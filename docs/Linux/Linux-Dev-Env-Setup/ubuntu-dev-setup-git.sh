#!/usr/bin/env bash
# ==============================================================================
# ENTERPRISE UBUNTU DEV ENVIRONMENT BOOTSTRAP
# - Repos (non-sudo)
# - Tools (sudo only when needed)
# - Docker + Minikube + Kubectl
# ==============================================================================

set -uo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <repos.conf> <tools.conf>"
  exit 1
fi

REPO_CONFIG="$1"
TOOLS_CONFIG="$2"
USER_HOME="$HOME"
REAL_USER="$USER"

info() { echo -e "\e[32m[INFO]\e[0m $1"; }
warn() { echo -e "\e[33m[WARN]\e[0m $1"; }
error() { echo -e "\e[31m[ERROR]\e[0m $1"; }

# ------------------------------------------------------------------------------
# SUDO AUTH (ONLY FOR INSTALLS)
# ------------------------------------------------------------------------------
info "Requesting sudo authentication..."
sudo -v || { error "Sudo authentication failed"; exit 1; }

(
  while true; do
    sudo -n true
    sleep 60
    kill -0 "$$" || exit
  done
) 2>/dev/null &

# ==============================================================================
# STEP 1: BASE PACKAGES
# ==============================================================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📦 STEP 1: Base System Setup"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

sudo apt update -y
sudo apt install -y \
  git curl wget gpg lsb-release \
  python3 python3-pip python3-venv \
  apt-transport-https ca-certificates \
  software-properties-common conntrack

# Ensure Flatpak
if ! command -v flatpak >/dev/null; then
  sudo apt install -y flatpak
  sudo flatpak remote-add --if-not-exists flathub \
    https://flathub.org/repo/flathub.flatpakrepo
fi

# Ensure Snap
if ! command -v snap >/dev/null; then
  sudo apt install -y snapd
fi

# ==============================================================================
# STEP 2: REPOSITORIES (NO SUDO HERE)
# ==============================================================================
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔧 STEP 2: Repository Checkout (User Context)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

while IFS='|' read -r NAME URL DEST USERNAME EMAIL OPEN; do
  [[ -z "$NAME" || "$NAME" =~ ^# ]] && continue

  DEST="${DEST/\/home\/user/$USER_HOME}"

  info "Processing repo: $NAME"

  mkdir -p "$DEST"

  if [[ ! -d "$DEST/.git" ]]; then
    git clone "$URL" "$DEST" || { warn "Clone failed: $NAME"; continue; }
  else
    (cd "$DEST" && git pull --rebase) || warn "Pull failed: $NAME"
  fi

  (
    cd "$DEST" || exit
    git config user.name "$USERNAME"
    git config user.email "$EMAIL"

    if [[ ! -d ".venv" ]]; then
      python3 -m venv .venv
    fi

    if [[ -f requirements.txt ]]; then
      ./.venv/bin/pip install --upgrade pip
      ./.venv/bin/pip install -r requirements.txt
    fi
  )

  if [[ "$OPEN" =~ ^[Yy]$ ]] && command -v code >/dev/null; then
    code "$DEST" &
  fi

done < "$REPO_CONFIG"

# ==============================================================================
# STEP 3: TOOL INSTALLATION (CONFIG DRIVEN)
# ==============================================================================
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📦 STEP 3: Installing Tools"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

APT_PACKAGES=()

while IFS='|' read -r TYPE PACKAGE EXTRA; do
  [[ -z "$TYPE" || "$TYPE" =~ ^# ]] && continue

  case "$TYPE" in
    APT)
      APT_PACKAGES+=("$PACKAGE")
      ;;
    SNAP)
      if [[ "$EXTRA" == "classic" ]]; then
        sudo snap install "$PACKAGE" --classic || warn "Snap failed: $PACKAGE"
      else
        sudo snap install "$PACKAGE" || warn "Snap failed: $PACKAGE"
      fi
      ;;
    FLATPAK)
      flatpak install -y flathub "$PACKAGE" || warn "Flatpak failed: $PACKAGE"
      ;;
  esac
done < "$TOOLS_CONFIG"

if [[ ${#APT_PACKAGES[@]} -gt 0 ]]; then
  sudo apt install -y "${APT_PACKAGES[@]}"
fi

# ==============================================================================
# STEP 4: DOCKER INSTALL (Official Method)
# Based on reference doc :contentReference[oaicite:0]{index=0}
# ==============================================================================
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🐳 STEP 4: Docker Installation"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if ! command -v docker >/dev/null; then
  sudo install -m 0755 -d /etc/apt/keyrings
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
    | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
  sudo chmod a+r /etc/apt/keyrings/docker.gpg

  echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

  sudo apt update
  sudo apt install -y docker-ce docker-ce-cli containerd.io \
    docker-buildx-plugin docker-compose-plugin
fi

sudo systemctl enable docker.service
sudo systemctl enable containerd.service

# Add user to docker group
sudo usermod -aG docker "$REAL_USER"

# Apply group immediately
newgrp docker <<EOF
echo "Docker group applied."
EOF

docker --version || warn "Docker verification failed"

# ==============================================================================
# STEP 5: KUBECTL INSTALL
# Based on reference doc :contentReference[oaicite:1]{index=1}
# ==============================================================================
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "☸️ STEP 5: Kubectl Installation"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if ! command -v kubectl >/dev/null; then
  curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
  sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
  rm kubectl
fi

kubectl version --client || warn "Kubectl verification failed"

# ==============================================================================
# STEP 6: MINIKUBE INSTALL
# Based on reference doc :contentReference[oaicite:2]{index=2}
# ==============================================================================
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🖥 STEP 6: Minikube Installation"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if ! command -v minikube >/dev/null; then
  curl -Lo minikube \
    https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
  sudo install minikube /usr/local/bin/
  rm minikube
fi

minikube version || warn "Minikube verification failed"

# ==============================================================================
# FINAL MESSAGE
# ==============================================================================
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ DEV ENVIRONMENT FULLY CONFIGURED"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "You can now run:"
echo "  docker run hello-world"
echo "  minikube start --driver=docker"
echo ""

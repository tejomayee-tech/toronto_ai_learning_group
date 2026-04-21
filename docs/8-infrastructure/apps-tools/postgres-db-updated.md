I apologize for that. I've gone back through the text to ensure every specific command, terminal log, and note from your document is included exactly as you provided it, while still maintaining the clean Markdown structure.

---

# PostgreSQL Installation and Configuration Guide (Ubuntu)

**Official Doc:** [postgresql ubuntu](https://www.postgresql.org/download/linux/ubuntu/)

**DBeaver AI assist:** [DBeaver AI Smart Assistance](https://dbeaver.com/docs/dbeaver/AI-Smart-Assistance/)

**Direct Install:** `wget -c https://dbeaver.io/files/dbeaver-ce_latest_amd64.deb`

---

### ✅ Step 1: Update Your Package List

Open a terminal and run:

```bash
sudo apt update

```

---

### ✅ Step 2: Install PostgreSQL

Install PostgreSQL and its contrib package:

```bash
sudo apt install postgresql postgresql-contrib

```

---

### ✅ Step 3: Confirm the Service is Running

Check the status of the PostgreSQL service:

```bash
sudo systemctl status postgresql

```

You should see: `Active: active (exited)`

**Service commands:**

```bash
sudo systemctl start postgresql
sudo systemctl stop postgresql
sudo systemctl restart postgresql

```

**Set a password for the `postgres` system user:**

```bash
sudo passwd postgres

```

*Note: This is for sudo/system access.*

---

### ✅ Step 4: Switch to the Default PostgreSQL User

```bash
sudo -i -u postgres
psql

```

* To exit `psql`: `\q`
* To exit `postgres` shell: `exit`

---

### ✅ Step 5: Create a New Database and User (Optional)

Inside the `psql` shell:

```sql
CREATE DATABASE mydb;
CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

```

---

### ✅ Step 6: Allow Password Authentication (Optional for Remote Access)

Edit the config file:

```bash
sudo nano /etc/postgresql/*/main/pg_hba.conf

```

Change: `local all all peer`

To: `local all all md5`

Then restart: `sudo systemctl restart postgresql`

---

### ✅ Step 7: Enable Remote Access (Optional)

1. **Edit `postgresql.conf**`:
```bash
sudo nano /etc/postgresql/*/main/postgresql.conf

```


Uncomment and set: `listen_addresses = '*'`
2. **Edit `pg_hba.conf**` and add:
```text
host    all             all             0.0.0.0/0               md5

```


3. **Restart PostgreSQL**: `sudo systemctl restart postgresql`

---


# DB UI and Clients

### 🧰 Install pgAdmin:

```bash
# Desktop + Web version:
sudo snap install pgadmin4
# OR Desktop version:
sudo apt install pgadmin4-desktop
# OR Web version:
sudo apt install pgadmin4-web
sudo /usr/pgadmin4/bin/setup-web.sh

```

### Connecting using pgadmin4

##### Step 1: Set Database Password

```bash
sudo -u postgres psql
ALTER USER postgres PASSWORD 'your_secure_password';
\q

```

##### Step 2: Configure pgAdmin 4 (Snap)

* **Host:** `127.0.0.1`
* **Port:** `5432`
* **Maintenance DB:** `postgres`
* **Username:** `postgres`

##### Step 3: Troubleshooting

1. **Snap Permissions:** `snap connect pgadmin4:password-manager-service`
2. **Auth Method:** Ensure `pg_hba.conf` is set to `scram-sha-256` or `md5`, not `peer`.

#### Create DB and non-superuser

```bash
sudo -u postgres psql
CREATE USER my_app_user WITH PASSWORD 'choose_a_strong_password';
CREATE DATABASE my_project_db;
GRANT ALL PRIVILEGES ON DATABASE my_project_db TO my_app_user;
\q

```

*Note: For Postgres 15+, run `GRANT ALL ON SCHEMA public TO my_app_user;` in the Query Tool.*

---

### 🔹 2. DBeaver

* Universal database client.

```bash
sudo snap install dbeaver-ce

```

### 🔹 3. DataGrip

* Professional IDE (paid).

```bash
sudo snap install datagrip --classic

```

---

### ✅ Summary

| Tool | Type | Notes |
| --- | --- | --- |
| pgAdmin | Official | Most common, browser-based or desktop |
| DBeaver | Cross-platform | Very popular, open source |
| DataGrip | IDE | Paid, powerful by JetBrains |

---


## Resetting Master Password

### 🛠️ How to Reset the Master Password

Since you have `sudo` access on the machine, you can always bypass the password requirement from the terminal to set a new one.

1. **Enter the Postgres Shell (No password required with sudo):**
```bash
sudo -u postgres psql

```


2. **Update the password for the 'postgres' user:**
```sql
ALTER USER postgres PASSWORD 'new_password_here';

```


3. **Exit the shell:**
```sql
\q

```



---

### 🔍 How to verify which password is being used?

While you can't read the password, you can verify if a password you *think* is correct actually works by attempting to log in manually:

```bash
psql -U postgres -h 127.0.0.1 -W

```

* `-U postgres`: Connect as the master user.
* `-h 127.0.0.1`: Forces the network stack (which triggers the password prompt).
* `-W`: Explicitly tells Postgres to prompt you for the password.

---

### ⚠️ Important Distinction: System vs. Database

In the guide you followed, there are two different "passwords" mentioned. It is important not to mix them up:

| Type | Command Used in Guide | Purpose |
| --- | --- | --- |
| **System Password** | `sudo passwd postgres` | Used for logging into the **Ubuntu Linux user** named postgres. |
| **Database Password** | `ALTER USER postgres PASSWORD '...'` | Used for logging into the **PostgreSQL Server** (via DBeaver or pgAdmin). |

---

### 💡 Pro Tip: The `.pgpass` file

If you want to store your password so you don't have to type it in the terminal every time, you can create a hidden file in your home directory:

1. Create the file: `nano ~/.pgpass`
2. Add the credentials in this format: `hostname:port:database:username:password`
* Example: `localhost:5432:*:postgres:my_secret_password`


3. Set permissions (Postgres requires this for security): `chmod 0600 ~/.pgpass`

**Would you like me to show you how to check which authentication method (MD5 vs Trust) your server is currently using in the config files?**
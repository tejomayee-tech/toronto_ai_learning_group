## Steps to install **PostgreSQL** on an **Ubuntu** system:

Also check [DBeaver AI assist](https://dbeaver.com/docs/dbeaver/AI-Smart-Assistance/)

Official Doc [postgresql ubuntu](https://www.postgresql.org/download/linux/ubuntu/)

install: wget -c https://dbeaver.io/files/dbeaver-ce_latest_amd64.deb 

---

### ✅ Step 1: Update Your Package List

Open a terminal and run:

```bash
sudo apt update
```

---

### ✅ Step 2: Install PostgreSQL

Install PostgreSQL and its contrib package (which provides additional features):

```bash
sudo apt install postgresql postgresql-contrib
```

---

### ✅ Step 3: Confirm the Service is Running

Check the status of the PostgreSQL service:

```bash
sudo systemctl status postgresql
```

You should see something like:

```
Active: active (exited)
```

To start/restart/stop the service, you can use:

```bash
sudo systemctl start postgresql
sudo systemctl stop postgresql
sudo systemctl restart postgresql
```


### **Set a password for the `postgres` system user**:

   ```bash
   sudo passwd postgres
   ```

   This will prompt you to enter a password for the `postgres` system user. You can choose any password here (it's just for `sudo` access).



### ✅ Step 4: Switch to the Default PostgreSQL User

PostgreSQL creates a default user named `postgres`. Switch to that user:

```bash
sudo -i -u postgres
```

Then you can access the PostgreSQL prompt using:

```bash
psql
```

To exit the `psql` prompt, type:

```sql
\q
```

To exit from the `postgres` user shell:

```bash
exit
```

---

### ✅ Step 5: Create a New Database and User (Optional)

Inside the `psql` shell, you can create a user and database like this:

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

Change this line:

```
local   all             all                                     peer
```

To:

```
local   all             all                                     md5
```

Then restart PostgreSQL:

```bash
sudo systemctl restart postgresql
```

---

### ✅ Step 7: Enable Remote Access (Optional)

1. Edit `postgresql.conf`:

```bash
sudo nano /etc/postgresql/*/main/postgresql.conf
```

Uncomment and set:

```
listen_addresses = '*'
```

2. Then edit `pg_hba.conf` again and add:

```
host    all             all             0.0.0.0/0               md5
```

3. Restart PostgreSQL again:

```bash
sudo systemctl restart postgresql
```

---
PostgreSQL itself doesn't come with a **built-in UI**, but yes — you can absolutely use a **graphical user interface (GUI)** on Ubuntu, just like on Windows. You just need to install one separately. Here are some popular PostgreSQL GUI tools you can use on Ubuntu:

---

### 🔹 1. **pgAdmin (Official UI)** 
> **Note**: difficult to install 

- The official and most full-featured GUI for PostgreSQL
- Can be run as a desktop app or in the browser (web app)

#### 🧰 Install pgAdmin on Ubuntu (Desktop Version):

Installs both desktop and web version and keep them up to date
```bash
sudo snap install pgadmin4
```

```bash
sudo apt install pgadmin4-desktop
```

Or for the web version:

```bash
sudo apt install pgadmin4-web
```

Then configure with:

```bash
sudo /usr/pgadmin4/bin/setup-web.sh
```


#### Connecting using pgadmin4


On Ubuntu, the **Snap** version of pgAdmin runs in a restricted sandbox, and the default `postgresql` installation uses "Peer" authentication, which doesn't allow external apps (like a Snap) to connect without a specific database password.

##### Step 1: Set a Database Password for the `postgres` User

The `sudo passwd postgres` command you ran only changed the **Linux system password** for that user; it did not change the **PostgreSQL database password**.

1. Open your terminal and enter the PostgreSQL prompt as the superuser:
```bash
sudo -u postgres psql

```


2. Now, set the database password by running this SQL command (replace `'your_secure_password'` with your actual password):
```sql
ALTER USER postgres PASSWORD 'your_secure_password';

```


3. Exit the prompt:
```sql
\q

```



---

##### Step 2: Configure pgAdmin 4 (Snap)

Launch your **pgAdmin 4** application and follow these steps to register your local server:

1. **Register Server:** Right-click on **Servers** > **Register** > **Server...**.
2. **General Tab:** Give it a name (e.g., `Localhost`).
3. **Connection Tab:** Use the following settings:
* **Host name/address:** `127.0.0.1` (using the IP is often more reliable than `localhost` for Snap apps).
* **Port:** `5432` (default).
* **Maintenance database:** `postgres`.
* **Username:** `postgres`.
* **Password:** The one you just set in **Step 1**.


4. **Save:** Click the **Save** button.

---

##### Step 3: Troubleshooting Connectivity

If pgAdmin fails to connect with a "Connection Refused" or "Peer Authentication Failed" error, check these two items:

1. Snap Permissions

Because pgAdmin is a Snap, it might need permission to talk to the local system. Run this command to ensure it can access necessary system services:

```bash
snap connect pgadmin4:password-manager-service

```

2. Check the Authentication Method

If you still get "Password authentication failed," you may need to ensure PostgreSQL is looking for a password rather than a Linux user match:

1. Open the configuration file:
```bash
sudo nano /etc/postgresql/$(psql --version | egrep -o '[0-9]{1,2}' | head -1)/main/pg_hba.conf

```


2. Find the line for `local` or `127.0.0.1` and ensure the method at the end is `scram-sha-256` or `md5`, **not** `peer`.
3. Restart PostgreSQL if you make changes:
```bash
sudo systemctl restart postgresql

```


#### Create DB and non-superuser

It is a best practice to avoid using the `postgres` superuser for daily tasks. Creating a dedicated user and database for your project adds a layer of security by limiting what that user can access.

You can do this directly inside **pgAdmin 4** or via the **Terminal**. Since you just set up the connection, using the Terminal is often the fastest way to ensure permissions are set correctly.

---

##### Step 1: Create the User and Database

Open your terminal and enter the PostgreSQL prompt again:

```bash
sudo -u postgres psql

```

Now, run the following SQL commands (replace the placeholders with your preferred names):

1. **Create a new user:**
```sql
CREATE USER my_app_user WITH PASSWORD 'choose_a_strong_password';

```


2. **Create the database:**
```sql
CREATE DATABASE my_project_db;

```


3. **Grant permissions:**
This gives your new user full control over the new database:
```sql
GRANT ALL PRIVILEGES ON DATABASE my_project_db TO my_app_user;

```


4. **Exit:**
```sql
\q

```



##### Step 2: Connect via pgAdmin 4

Now that the database and user exist, you should add a second connection in pgAdmin specifically for this user. This mimics how a real application (like a Python or Node.js app) would connect.

1. Open **pgAdmin 4**.
2. Right-click **Servers** > **Register** > **Server...**
3. **General Tab:** Name it `My Project DB`.
4. **Connection Tab:**
* **Host:** `127.0.0.1`
* **Port:** `5432`
* **Maintenance database:** `my_project_db` (Type your new DB name here).
* **Username:** `my_app_user`
* **Password:** The password you chose in Step 1.


5. **Save.**


##### Step 3: Verify Permissions (The Schema Test)

By default, in PostgreSQL 15 and later, you may need to explicitly grant permission to create tables within the `public` schema of your new database.

If you try to create a table and get a "Permission Denied" error, run this one-time fix:

1. In pgAdmin, right-click your new database (`my_project_db`).
2. Select **Query Tool**.
3. Run this command:
```sql
GRANT ALL ON SCHEMA public TO my_app_user;

```




##### Why do this?

* **Safety:** If you accidentally run a "Drop Table" command or a buggy script, you only risk the specific project database, not the entire PostgreSQL system.
* **Security:** If your application's credentials are ever leaked, the attacker only gains access to that one database, rather than full administrative control over your server.


---

### 🔹 2. **DBeaver**

- Universal database client
- Works with PostgreSQL, MySQL, SQLite, and many more
- Nice UI and popular among developers

#### 🧰 Install DBeaver (Community Edition):

```bash
sudo snap install dbeaver-ce
```

Or use their `.deb` package from [dbeaver.io](https://dbeaver.io/download/)

---

### 🔹 3. **DataGrip** (JetBrains)

- Powerful professional database IDE (paid)
- Great for advanced PostgreSQL management
- Supports all major databases

#### 🧰 Install via JetBrains Toolbox or:

```bash
sudo snap install datagrip --classic
```

---

### ✅ Summary

| Tool        | Type        | Notes                        |
|-------------|-------------|------------------------------|
| pgAdmin     | Official    | Most common, browser-based or desktop |
| DBeaver     | Cross-platform | Very popular, open source    |
| DataGrip    | IDE         | Paid, powerful by JetBrains  |

---

## Actual config steps

vijay@vijay-UbuntuLTS:~$ sudo snap install dbeaver-ce
dbeaver-ce 25.0.2.202504061727 from DBeaver (dbeaver-corp) installed
vijay@vijay-UbuntuLTS:~$ sudo -i -u postgres
postgres@vijay-UbuntuLTS:~$ psql
psql (16.8 (Ubuntu 16.8-1.pgdg22.04+1))
Type "help" for help.

postgres=# CREATE ROLE dbadmin WITH LOGIN PASSWORD 'dbadmin@123';
CREATE ROLE
postgres=# \q
postgres@vijay-UbuntuLTS:~$ sudo nano /etc/postgresql/*/main/pg_hba.conf
[sudo] password for postgres: 
Sorry, try again.
[sudo] password for postgres: 
Sorry, try again.
[sudo] password for postgres: 
sudo: 2 incorrect password attempts
postgres@vijay-UbuntuLTS:~$ sudo nano /etc/postgresql/*/main/pg_hba.conf
[sudo] password for postgres: 
Sorry, try again.
[sudo] password for postgres: 
sudo: 1 incorrect password attempt
postgres@vijay-UbuntuLTS:~$ whoami
postgres
postgres@vijay-UbuntuLTS:~$ exit
logout
vijay@vijay-UbuntuLTS:~$ sudo passwd postgres
New password: 
Retype new password: 
passwd: password updated successfully
vijay@vijay-UbuntuLTS:~$ sudo -i -u postgres
postgres@vijay-UbuntuLTS:~$ sudo nano /etc/postgresql/*/main/pg_hba.conf
[sudo] password for postgres: 
postgres is not in the sudoers file.
postgres@vijay-UbuntuLTS:~$ exit
logout
vijay@vijay-UbuntuLTS:~$ sudo visudo
vijay@vijay-UbuntuLTS:~$ sudo visudo
visudo: /etc/sudoers.tmp unchanged
vijay@vijay-UbuntuLTS:~$ sudo -i -u postgres
postgres@vijay-UbuntuLTS:~$ sudo nano /etc/postgresql/*/main/pg_hba.conf
[sudo] password for postgres: 
postgres@vijay-UbuntuLTS:~$ sudo systemctl restart postgresql
Warning: The unit file, source configuration file or drop-ins of postgresql.service changed on disk. Run 'systemctl daemon-reload' to reload units.
postgres@vijay-UbuntuLTS:~$ systemctl daemon-reload
postgres@vijay-UbuntuLTS:~$ 

## login with dbadmin/badmin@123
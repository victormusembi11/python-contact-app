# python-demo

## Install mysql

### Linux

```bash
sudo apt-get install mysql-server
```

### Mac

```bash
brew install mysql
```

## Run DB Migration

Login to mysql

```bash
mysql -u root -p
```

Source the migration file

```bash
source app/schema.sql
```

## Create a virtual environment

```bash
python3 -m venv venv
```

## Activate the virtual environment

```bash
source venv/bin/activate
```

## Set environment variables

Create a `.env` file in the root directory of the project and add the following variables

```bash
DB_USER=root
DB_PASS=your-password
DB_HOST=localhost
DB_NAME=PyContacts
DB_RAISE_ON_WARNING=True
```

## Install python dependencies

```bash
pip install -r requirements.txt
```

## Run the app

```bash
python main.py
```

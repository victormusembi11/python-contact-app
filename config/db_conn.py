import mysql.connector

from config.utils import get_env_variable, get_bool_env

config = {
    "user": get_env_variable("DB_USER"),
    "password": get_env_variable("DB_PASS"),
    "host": get_env_variable("DB_HOST"),
    "database": get_env_variable("DB_NAME"),
    "raise_on_warnings": get_bool_env("DB_RAISE_ON_WARNINGS"),
}

cnx = mysql.connector.connect(**config)

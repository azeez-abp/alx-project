import MySQLdb  # type: ignore
from MySQLdb import MySQLError
import os
from app.models.storage_engine.db import DBStorage


class ConnectMysqlDB:
    """Connect to MySQL database and create it if it does not exist."""
    __has_connected = False

    def __init__(self):
        """Instantiate a DBStorage object and create \
            the database if necessary."""
        self.MYSQL_USER = os.getenv('MYSQL_USER')
        self.MYSQL_PWD = os.getenv('MYSQL_PWD')
        self.MYSQL_HOST = os.getenv('MYSQL_HOST')
        self.MYSQL_DB = os.getenv('MYSQL_DB')

        print(f"Connecting to MySQL host: {self.MYSQL_HOST}")

        self.create_database_if_not_exists()

    def create_database_if_not_exists(self):
        """Create the database if it does not exist."""
        count = 0
        while count < 10:
            try:
                conn = MySQLdb.connect(
                    host=self.MYSQL_HOST,
                    user=self.MYSQL_USER,
                    passwd=self.MYSQL_PWD
                )
                cursor = conn.cursor()
                cursor.execute(f"CREATE DATABASE IF NOT\
                                EXISTS {self.MYSQL_DB}")
                conn.commit()
                conn.close()
                ConnectMysqlDB.__has_connected = True
                print(f"Database {self.MYSQL_DB} ensured.")
                break
            except MySQLError as e:
                print(f"Failed to connect or create database: {e}, \
                      attempt {count + 1}")
                count += 1
                if count >= 10:
                    print("Max retries reached. Could not \
                          establish a connection.")

    @staticmethod
    def has_connected():
        return ConnectMysqlDB.__has_connected


# Instantiate and initialize the DBStorage if connection was successful
db_connection = ConnectMysqlDB()
if ConnectMysqlDB.has_connected():
    storage = DBStorage()
    storage.reload()

else:
    print("Failed to connect to the database. DBStorage not initialized.")

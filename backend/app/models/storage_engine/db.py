#!/usr/bin/python3
"""
Contains the class DBStorage
"""
from os import getenv
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.orm import scoped_session, sessionmaker  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore


Base = declarative_base()


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None  # type: ignore
    __session = None  # type: ignore

    def __init__(self):
        """Instantiate a DBStorage object"""
        MYSQL_USER = getenv('MYSQL_USER')
        MYSQL_PWD = getenv('MYSQL_PWD')
        MYSQL_HOST = getenv('MYSQL_HOST')
        MYSQL_DB = getenv('MYSQL_DB')
        APP_ENV = getenv('APP_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MYSQL_USER,
                                             MYSQL_PWD,
                                             MYSQL_HOST,
                                             MYSQL_DB))
        if APP_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def get_instance(self):
        return self.__session

    def get_engine(self):
        return self.__engine

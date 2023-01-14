from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DBConfig:

    def __init__(self):
        self.__user: str
        self.__password: str
        self.__host: str
        self.__db: str
        self.__port: int

        self.__conn: str

        if config('PROD', cast=bool):
            ...

        else:
            self.__user = config('DBUSER', cast=str)
            self.__password = config('DBPASSWORD', cast=str)
            self.__host = config('DBHOST', cast=str)
            self.__db = config('DB', cast=str)
            self.__port = config('DBPORT', cast=int)

            self.__conn = 'postgresql://%s:%s@%s:%d/%s' /
                          % (
                            self.__user,
                            self.__password,
                            self.__host,
                            self.__port,
                            self.__db
                      )

            self.__engine = create_engine(
                self.__conn,
                echo=True if not config('PROD', cast=bool) else False
            )

            self.__session = sessionmaker(bind=self.__engine)()
            self.__base = declarative_base()

    @property
    def session(self):
        return self.__session

    @property
    def base(self):
        return self.__base

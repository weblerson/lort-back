from fastapi import FastAPI
from decouple import config


class Config:
    def __init__(self):
        self.__app: FastAPI
        if config('PROD', cast=bool):
            self.__app = FastAPI(docs_url=None, redoc_url=None)

        else:
            self.__app = FastAPI()

    @property
    def app(self) -> FastAPI:
        return self.__app

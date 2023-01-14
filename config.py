from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config


class Config:
    def __init__(self):
        self.__app: FastAPI
        if config('PROD', cast=bool):
            self.__app = FastAPI(docs_url=None, redoc_url=None)

        else:
            self.__app = FastAPI()

        origins = config('ORIGINS', cast=list[str])
        methods = config('METHODS', cast=list[str])
        self.__app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=methods,
            allow_headers=['Token']
        )

    @property
    def app(self) -> FastAPI:
        return self.__app


from fastapi import FastAPI
from api.config.config import Config

app = FastAPI()

config = Config()

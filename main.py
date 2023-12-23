from fastapi import FastAPI
from api.config import config

app = FastAPI()

config = config()

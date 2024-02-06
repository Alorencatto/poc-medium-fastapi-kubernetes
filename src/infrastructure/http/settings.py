import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

root_path = os.getenv("ENV", default="")


class Settings(BaseSettings):
    title: str = "FastAPI Clean Architecture Medium Kubernetes POC"
    version: str = "0.0.1"
    openapi_url: str = "/openapi.json"
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    root_path: str = f"/{root_path}"

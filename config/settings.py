import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    POSTGRES_VERSION=os.getenv("POSTGRES_VERSION")
    DATABASE_USER=os.getenv("DATABASE_USER")
    DATABASE_PASSWORD=os.getenv("DATABASE_PASSWORD")
    DATABASE_DB=os.getenv("DATABASE_DB")
    DATABASE_SERVER=os.getenv("DATABASE_SERVER")
    DATABASE_PORT=os.getenv("DATABASE_PORT")

    PYTHON_VERSION=os.getenv("PYTHON_VERSION")

    DEBUG = os.getenv("DEBUG", "False") == "True"

settings = Settings()

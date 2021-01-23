import os
from dotenv import load_dotenv

load_dotenv()

base_dir = os.path.abspath(os.getcwd())


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('secret')


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{base_dir}/dev1.db"
    DEBUG = True


config = {
    "development":DevConfig,
    "default": DevConfig
}

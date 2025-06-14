import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bugtracker.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

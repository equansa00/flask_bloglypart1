import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'postgresql://postgres:1Chriss1@localhost/blogly'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # any other configurations can be added here...

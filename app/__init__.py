"""
app/__init__.py: Application init file, enables import of module
"""

from flask import Flask
from config import Config

app = Flask(__name__)

#set application security key
app.config.from_object(Config)
from app import routes
"""
__init__.py: Main initialization file for tha application
"""

from flask import Flask

app = Flask(__name__)

from app import routes

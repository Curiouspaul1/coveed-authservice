from flask import Blueprint

doc = Blueprint(__name__, 'doc')

from . import views

from flask import Blueprint


wb = Blueprint("wb", __name__)

from .views import index, user
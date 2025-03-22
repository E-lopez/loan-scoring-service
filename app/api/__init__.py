from flask import Blueprint

bp = Blueprint('routes', __name__, url_prefix='/scoring')

from app.api import routes
from venv import logger
from flask import Blueprint, jsonify, request, flash, redirect
import requests

from services.register_survey_service import register_survey_method

routes = Blueprint('routes', __name__, url_prefix='/scoring')

@routes.route("/")
def home():
  return "Hi there mofos Scoring Here"

@routes.post("/survey")
def register_survey():
  data = request.get_json()
  return register_survey_method(data)


    
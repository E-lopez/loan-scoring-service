from venv import logger
from flask import Blueprint, jsonify, request, flash, redirect
import requests

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from services.register_survey_service import register_survey_method

routes = Blueprint('routes', __name__, url_prefix='/scoring')
db = SQLAlchemy()

@routes.route("/")
def home():
  return "Hi there mofos Scoring Here"


@routes.post("/survey")
def register_survey():
  data = request.get_json()
  return register_survey_method(data)


@routes.route('/db')
def testdb():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
import random
from app.api import bp
from app.extensions import db
from flask import request

from services.amortization_service import repayment_plan
from services.register_survey_service import register_survey_method


@bp.route("/")
def home():
  db.create_all()
  return "Create all method"


@bp.route("/drop")
def temp():
  db.drop_all()
  return "Drop all method"


@bp.post("/survey")
def register_survey():
  data = request.get_json()
  return register_survey_method(data)


@bp.post("/repayment-plan")
def generate_table():
  data = request.get_json()
  return repayment_plan(data)

import random
from app.api import bp
from app.extensions import db
from flask import request

from app.models.userAmortizationData import UserAmortizationData
from services.amortization_service import recalculate_plan, repayment_plan
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


@bp.route("/repayment-plan/<user_id>")
def get_user_amortization(user_id):
  user_data = db.session.execute(
    db.select(UserAmortizationData).filter_by(userId=user_id)
  ).scalar_one_or_none()
  if user_data is None:
    return {"error": "User not found"}, 404
  return recalculate_plan(user_data), 200

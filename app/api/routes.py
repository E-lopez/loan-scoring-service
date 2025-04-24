import random
from app.api import bp
from app.extensions import db
from flask import request, jsonify

from app.models.userScore import UserScore
from services.amortization_service import repayment_plan
from services.register_survey_service import register_survey_method
from app.models.post import Post

@bp.route("/")
def home():
  db.create_all()
  return "Create all method"


@bp.route("/drop")
def temp():
  db.drop_all()
  return "Drop all method"


@bp.route("/add", methods=('GET', 'POST'))
def add_posts():
  scores = UserScore.query.all()
  print(request.method)
  if request.method == 'POST':
    new_score = UserScore(name='Pepito', score=8)
    db.session.add(new_score)
    db.session.commit()
    return 'Score saved correctly'
  return jsonify([u.toDict() for u in scores])


@bp.post("/survey")
def register_survey():
  data = request.get_json()
  return register_survey_method(data)


@bp.post("/repayment-plan")
def generate_table():
  data = request.get_json()
  return repayment_plan(data)


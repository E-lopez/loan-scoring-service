import random
from app.api import bp
from app.extensions import db
from flask import request

from services.register_survey_service import register_survey_method
from app.models.post import Post

@bp.route("/")
def home():
  db.create_all()
  return "Hi there mofos Scoring Here"

@bp.route("/add")
def add_posts():
  posts = Post.query.all()
  return posts.to_string()


@bp.post("/survey")
def register_survey():
  data = request.get_json()
  return register_survey_method(data)

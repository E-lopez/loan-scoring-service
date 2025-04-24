from venv import logger
from flask import jsonify
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError

from app.extensions import db

from app.models.userScore import UserScore
from utils.question_scoring import QuestionScoring
from utils.section_weight_map import get_question_weight
from utils.table_generator import TableGenerator   


def repayment_plan(data):
  payment_type = data.pop('payment_type')
  repayment_type = 'repayment_plan_period' if payment_type == 'period' else 'repayment_plan_instalment'
  generator = TableGenerator(repayment_type)
  res = generator.use_method(**data)
  print(res)
  return res  

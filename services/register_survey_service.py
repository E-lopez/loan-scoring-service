from venv import logger
from flask import jsonify
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError

from app.extensions import db

from app.models.userScore import UserScore
from utils.question_scoring import QuestionScoring
from utils.section_weight_map import get_question_weight   


def calc_score(section, values):
  res = {}
  scoring = QuestionScoring(section)
  scoring_res = scoring.use_scoring(values)
  weight = 0.3 if section == 'demographics' else values['weight']
  res[section] = scoring_res * weight
  return res


def register_survey_method(data):
  id_number = data['demographics']['idNumber']
  parsed_data = {'demographics': {**data['demographics']}, **data['sections']}

  t = list(map(lambda x: calc_score(x[0], x[1]), parsed_data.items()))
  scores = {k: v for dict in t for k, v in dict.items()}
  sum_scr = sum(scores.values())

  new_score = UserScore(
    userId = id_number,
    demographics = scores['demographics'],
    financialKnowledge = scores['financialKnowledge'],
    riskTolerance = scores['riskTolerance'],
    trustLevel = scores['trustLevel'],
    risk_level = sum_scr
  )

  try:
    db.session.add(new_score)
    db.session.flush()
    db.session.commit()
    res = db.session.execute(db.select(UserScore).filter_by(userId=id_number)).scalar_one()
    print(res.toDict())
    return res.toDict()
  except SQLAlchemyError as e:
    error = str(e.__dict__['orig'])
    return error
  
   

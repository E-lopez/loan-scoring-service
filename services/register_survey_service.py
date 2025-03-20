from venv import logger
import pandas as pd

from utils.question_scoring import QuestionScoring
from utils.section_weight_map import get_question_weight   


def test(section, values):
  res = {}
  scoring = QuestionScoring(section)
  scoring_res = scoring.use_scoring(values)
  weigth = get_question_weight(section)
  res[section] = scoring_res * weigth
  return res


def register_survey_method(data):
  id_number = {'id': data['demographics']['idNumber']}
  t = list(map(lambda x: test(x[0], x[1]), data.items()))
  scores = {k: v for dict in t for k, v in dict.items()}
  sum_scr = {'level': sum(scores.values())}
  res = {**id_number, **scores, **sum_scr}

  df = pd.DataFrame(res, index=[0])
  print(df)
    
  return df.to_string()
   
   
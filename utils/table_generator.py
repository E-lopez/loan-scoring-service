from __future__ import annotations
from abc import ABC, abstractmethod
from math import ceil
from operator import itemgetter
from typing import List
from venv import logger
from flask import jsonify
from datetime import date
import pandas as pd
import numpy_financial as npf

from sqlalchemy.exc import SQLAlchemyError

from app.extensions import db

from app.models.userScore import UserScore
from utils.functions import cast_value, map_risk_to_rate
from utils.question_scoring import QuestionScoring
from utils.section_weight_map import get_question_weight   


class TableGenerator():
  def __init__(self, strategy = None) -> None:
    self._strategy = self.select_method(strategy)

  def select_method(self, strategy):
    match strategy:
      case 'repayment_plan_period':
        return GenerateByPeriod()
      case 'repayment_plan_instalment':
        return GenerateByInstalment()
      case _:
        return 'Not Implemented'
      
  def set_method(self, strategy: Strategy):
    self._strategy = strategy

  def use_method(self, **kwargs):
    return self._strategy.generate_table(**kwargs)


class Strategy(ABC):
  @abstractmethod
  def generate_table(self, **kwargs: List):
    pass


class GenerateByPeriod(Strategy):
  def generate_table(self, **kwargs):
    t = {
      k: (lambda k, x=v: cast_value(k, x) if x != 'null' else x)
      (k, v) for k, v in kwargs.items()
    }
    user_risk, period, amount = itemgetter('user_risk', 'period', 'amount')(t)
    r = map_risk_to_rate(user_risk)

    rng = pd.date_range(date.today(), periods = period, freq='MS')
    rng.name = "Payment_Date"

    df = pd.DataFrame(index=rng,columns=['Payment', 'Principal', 'Interest', 'Balance'], dtype=object)
    df.reset_index(inplace=True)
    df.index.name = "Period"
    df.index += 1

    df['Payment'] = npf.pmt(r/12, period, amount)
    df['Principal'] = npf.ppmt(r/12, df.index, period, amount)
    df['Interest'] = npf.ipmt(r/12, df.index, period, amount)
    df['Balance'] = amount + df['Principal'].cumsum()

    df.iloc[:, 1:] = df.iloc[:, 1:].map(lambda x: ceil(abs(x)))
    return df.to_string()


class GenerateByInstalment(Strategy):
  def generate_table(self, **kwargs):
    t = {
      k: (lambda k, x=v: cast_value(k, x) if x != 'null' else x)
      (k, v) for k, v in kwargs.items()
    }
    user_risk, instalment, amount = itemgetter('user_risk', 'instalment', 'amount')(t)
    r = map_risk_to_rate(user_risk)

    res = {}

    return res  

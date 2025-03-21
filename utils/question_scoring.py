from __future__ import annotations
from abc import ABC, abstractmethod
import locale
from typing import List
from models.defaults.defaults_dict import document_defaults
from utils.functions import get_default
import re

loc = locale.getlocale()
locale.setlocale(locale.LC_MONETARY, loc)

class QuestionScoring():
  def __init__(self, strategy = None) -> None:
    self._strategy = self.select_scoring(strategy)

  def select_scoring(self, strategy):
    match strategy:
      case 'demographics':
        return DemographicsScoring()
      case _:
        return Default()

  def set_scoring(self, strategy: Strategy):
    self._strategy = strategy

  def use_scoring(self, *args):
    return self._strategy.score_question(*args)


class Strategy(ABC):
  @abstractmethod
  def score_question(self, *args: List):
    pass


class Default(Strategy):
  def __init__(self):
        self.count = 0
        self.data = dict()

  def score_question(self, *args, i = 0):
    if(len(self.data) == 0):
      self.data = {**self.data, **(dict(args[0]))}
    if(i == len(self.data)):
      return self.count
    key = list(self.data)[i]
    partial = self.data[key] if type(self.data[key]) == 'int' else 3
    self.count = self.count + partial
    return self.score_question(self, args, i = i+1)


class DemographicsScoring(Strategy):
  def __init__(self):
        self.count = 0
        self.data = dict()

  def field_score(self, key) -> float:
    data = self.data[key]
    match key:
      case 'dateOfBirth':
        return 3.0
      case 'gender':
        return 3.0 if data == 'M' else 2.0
      case 'occupation':
        return 3.0 if data == 'Empleado' else 1.0
      case _:
        return 0.0

  def score_question(self, *args, i = 0):
    if(len(self.data) == 0):
      self.data = {**self.data, **(dict(args[0]))}
    if(i == len(self.data)):
      return self.count
    key = list(self.data)[i]
    self.count = self.count + self.field_score(key)
    return self.score_question(self, args, i = i+1)
       
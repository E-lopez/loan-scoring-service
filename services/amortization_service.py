from sqlalchemy.exc import SQLAlchemyError
from app.models.userAmortizationData import UserAmortizationData
from app.models.userScore import UserScore
from utils.table_generator import TableGenerator 
from app.extensions import db
import logging

def get_user_risk(user_id):
  try:
    res = db.session.execute(
      db.select(UserScore.risk_level).filter_by(userId=user_id)
    ).scalar_one()
    return res
  except SQLAlchemyError as e:
    error = str(getattr(e, 'orig', e))
    return error
  

def save_amortization(user_id, user_risk, period_value, instalment_value, amount):
  data = UserAmortizationData(
    userId=user_id,
    userRisk=user_risk,
    instalment=instalment_value,
    period=period_value,
    amount=amount
  )
  try:
    db.session.add(data)
    db.session.flush()
    db.session.commit()
    res = db.session.execute(db.select(UserAmortizationData).filter_by(userId=user_id)).scalar_one()
    return res.toDict()
  except SQLAlchemyError as e:
    error = str(getattr(e, 'orig', e))
    logging.error(f"Error saving amortization data: {error}")
    return error
  

def handle_amortization(user_id, data):
  user_data = UserAmortizationData.query.filter_by(userId=user_id).first()
  user_risk = get_user_risk(user_id)
  period_value = data.get('period') if data.get('period') != "null" else 0
  instalment_value = data.get('instalment') if data.get('instalment') != "null" else 0
  amount = data['amount']

  if user_data is None:
    save_amortization(user_id, user_risk, period_value, instalment_value, amount)
  else:
    user_data.userRisk = user_risk
    user_data.period = period_value
    user_data.instalment = instalment_value
    user_data.amount = amount
    db.session.commit()


def repayment_plan(data):
  payment_type = data.pop('payment_type')
  user_id = data.pop('userId')
  repayment_type = 'repayment_plan_period' if payment_type == 'period' else 'repayment_plan_instalment'
  handle_amortization(str(user_id), data)
  generator = TableGenerator(repayment_type)
  res = generator.use_method(**data)
  return res  

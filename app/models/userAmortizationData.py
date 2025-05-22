from app.extensions import db
class UserAmortizationData(db.Model):
    nrow = db.Column(db.Integer, primary_key=True)
    userId= db.Column(db.String(150), nullable=False, unique=True)
    userRisk= db.Column(db.Float)
    instalment= db.Column(db.Float)
    period= db.Column(db.Float)
    amount= db.Column(db.Float)

    def toDict(self):
        return dict(
            userId=self.userId,
            userRisk=self.userRisk,
            instalment=self.instalment,
            period=self.period,
            amount=self.amount            
        )
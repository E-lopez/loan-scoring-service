from app.extensions import db
class UserScore(db.Model):
    nrow = db.Column(db.Integer, primary_key=True)
    userId= db.Column(db.String(150), nullable=False, unique=True)
    demographics = db.Column(db.Float)
    financialKnowledge = db.Column(db.Float)
    riskTolerance = db.Column(db.Float)
    trustLevel = db.Column(db.Float)
    risk_level = db.Column(db.Float)

    def toDict(self):
        return dict(
            userId=self.userId,
            demographics=self.demographics,
            financialKnowledge=self.financialKnowledge,
            riskTolerance=self.riskTolerance,
            trustLevel=self.trustLevel,
            riskLevel=self.risk_level,
        )
from app.extensions import db
class UserScore(db.Model):
    nrow = db.Column(db.Integer, primary_key=True)
    userId= db.Column(db.String(150), nullable=False, unique=True)
    demographics = db.Column(db.Float)
    financialResponsibility = db.Column(db.Float)
    riskAversion = db.Column(db.Float)
    impulsivity = db.Column(db.Float)
    futureOrientation = db.Column(db.Float)
    financialKnowledge = db.Column(db.Float)
    locusOfControl = db.Column(db.Float)
    socialInfluence = db.Column(db.Float)
    resilience = db.Column(db.Float)
    familismo = db.Column(db.Float)
    respect = db.Column(db.Float)
    risk_level = db.Column(db.Float)

    def toDict(self):
        return dict(
            userId=self.userId,
            demographics=self.demographics,
            financialResponsibility=self.financialResponsibility,
            riskAversion=self.riskAversion,
            impulsivity=self.impulsivity,
            futureOrientation=self.futureOrientation,
            financialKnowledge=self.financialKnowledge,
            locusOfControl=self.locusOfControl,
            socialInfluence=self.socialInfluence,
            resilience=self.resilience,
            familismo=self.familismo,
            respect=self.respect,
            riskLevel=self.risk_level,
        )
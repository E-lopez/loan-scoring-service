from app.extensions import db

class UserScore(db.Model):
    nrow = db.Column(db.Integer, primary_key=True)
    userId= db.Column(db.String(150), nullable=False, unique=True)
    demographics = db.Column(db.Float)
    section_1 = db.Column(db.Float)
    section_2 = db.Column(db.Float)
    risk_level = db.Column(db.Float)

    def toDict(self):
        return dict(
            userId=self.userId,
            demographics=self.demographics,
            section1=self.section_1,
            section2=self.section_2,
            riskLevel=self.risk_level,
        )
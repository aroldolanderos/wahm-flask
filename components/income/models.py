from database import db
from datetime import datetime


class Income(db.Model):
    __tablename__ = 'incomes'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250), nullable=True)
    amount = db.Column(db.Float(), nullable=False)
    currency = db.Column(db.String(7), nullable=True, default='CLP')
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow()
    )

    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def __repr__(self):
        return f"{self.description}: ${self.amount}"

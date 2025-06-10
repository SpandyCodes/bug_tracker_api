from models import db

class Bug(db.Model):
    __tablename__ = 'bugs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(10), nullable=False)  # Low, Medium, High
    status = db.Column(db.String(20), default='Open')     # Open, In Progress, Done
    progress = db.Column(db.Integer, default=0)           # 0 - 100
    comments = db.Column(db.Text)

    assigned_to = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

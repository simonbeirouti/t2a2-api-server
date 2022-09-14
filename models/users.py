from main import db

# Create a model for the users table
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    dob = db.Column(db.Date(), nullable=False)
    country = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(), nullable=False)
    suburb = db.Column(db.String(), nullable=False)
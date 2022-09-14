from flask import Blueprint
from main import db
from models.users import User
from datetime import date

db_cmd = Blueprint('db', __name__)

# Create databases from the models
@db_cmd.cli.command('create')
def create_db():
    db.create_all()
    print('Database created')

# Drop databases from the models
@db_cmd.cli.command('drop')
def drop_db():
    db.drop_all()
    print('Database dropped')

# Seed the database
@db_cmd.cli.command('seed')
def seed_db():
    # Array with users
    users = [
        ['Simon', 'Beirouti', 'hi@e.com', '123qwe123', 17, 11, 1992, 'Australia', 'Victoria', 'Dandenong'],
        ['Clive', 'Palmer', 'cp@e.com', '123qwe123', 26, 3, 1954, 'Australia', 'Victoria', 'Footscray'],
        ['Daniel', 'Andrews', 'da@e.com', '123qwe123', 6, 7, 1972, 'Australia', 'Victoria', 'Williamstown'],
        ['Kevin', 'Rudd', 'kr@e.com', '123qwe123', 21, 9, 1957, 'Australia', 'Queensland', 'Nambour'],
        ['Julia', 'Gillard', 'jg@e.com', '123qwe123', 29, 9, 1961, 'Wales', 'Vale of Glamorgan', 'Barry']]
    # Loop through the array and add the users
    for user in users:
        # Create the user
        new_user = User(
            first_name = user[0],
            last_name = user[1],
            email = user[2],
            password = user[3],
            dob = date(day = user[4], month = user[5], year = user[6]),
            country = user[7],
            state = user[8],
            suburb = user[9]
        )
        # Add the user to the database
        db.session.add(new_user)
    # Commit the changes
    db.session.commit()
    print('Database seeded')
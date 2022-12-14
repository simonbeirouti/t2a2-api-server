# import os 
# from flask import send_from_directory     
from datetime import timedelta
from flask import Blueprint, request
from main import db, bc
from flask_jwt_extended import create_access_token
from models.users import User
from schemas.user_schema import user_schema

main = Blueprint("auth", __name__)

# Route for the index page to contain information that the user of API can refer to
@main.route("/")
def main_page():
    return {
        "Welcome": "This is a job portal API.", 
        "How to use": "The following inforamtion contains the various routes and how to interact with the API.",
        "routes": [{
            "/": "THe home route and where this informaiton is located!",
            "/login": [{
                "info": "Where you can login in to your account",
                "POST": "You can make a POST request to log into your account.",
                "request" : [{
                    "email": "hi@email.com",
                    "password": "example"
                }]
            }],
            "/register": [{
                "info": "Where you can create an account to get started!",
                "POST" : "Make a POST request to create an account",
                "request": [{
                    "first_name": "Simon",
                    "last_name": "Beirouti",
                    "email": "hi@email.com",
                    "pasword": "example",
                    "dob": "2000-1-1",
                    "country": "Australia",
                    "state": "Victoria",
                    "suburb": "Dandenong"
                }]
            }],
            "/jobs": [{
                "info": "Get a list of all the jobs available.",
                "GET": "Will get you all the job postings on the server"
            }],
            "/admin": "allow the user to edit their preferences.",
            "/company": "display the various companies that have job postings.",
        }]
    }

# Setup the register route so users can create an account
@main.route("/register", methods=["POST"])
def register_user():
    user_fields = user_schema.load(request.json)
    user = User.query.filter_by(email = user_fields["email"]).first()
    if user:
        return {"error": "Email already exists."}, 400
    user = User(
        email = user_fields["email"],
        password = bc.generate_password_hash(user_fields["password"]).decode("utf-8"),
    )
    db.session.add(user)
    db.session.commit()
    token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1))
    return {"username": user.email, "token": token}, 200

# Setup the login route so users can sign into their account
@main.route("/login", methods=["POST"])
def login_user():
    user_fields = user_schema.load(request.json)
    user = User.query.filter_by(email=user_fields["email"]).first()
    if not user:
        return {"error": "email is not valid."}, 404
    if not bc.check_password_hash(user.password, user_fields["password"]):
        return {"error": "Password is not valid."}, 404
    token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1))
    return {"username": user.email, "token": token}, 200

# Setup the jobs route so anyone can get a list of the jobs posted
# @main.route('/jobs', methods=["GET"])
# def jobs_page():


# add route to fix favicon error
# @main.route('/favicon.ico') 
# def favicon(): 
#     return send_from_directory(os.path.join(main.root_path, 'static'), 'favicon.ico', mimetype='image/ico')
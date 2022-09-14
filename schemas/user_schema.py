from main import ma 
from marshmallow.validate import Length
import re

# regex requirements for the email
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

# Function to check if the email is valid
def isValid(email):
    if re.fullmatch(regex, email):
      return True
    else:
      return False

# Create a schema for the users table
class UserSchema(ma.Schema):
    class Meta:
        # Order the fields in order of id
        ordered = True
        # Fields to expose
        fields = ("user_id", "first_name", "last_name", "email", "password", "dob", "country", "state", "suburb")
    # Validation from marshmallow
    password = ma.String(validate=Length(min=8))
    # Validation for the email. Check via the regex function if it's valid
    email = ma.String(validate=isValid, required = True)

user_schema = UserSchema()
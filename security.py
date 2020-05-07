from werkzeug.security import safe_str_cmp
from models.user import User


def authenticate(username, password):
    user = User.find_by_username(username) #use get method to have a default value in case of None
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
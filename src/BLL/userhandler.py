from Models import User
from DAL import get_user
from DAL import set_user



def sign_in(username,password,user_db):

    user=get_user(username,user_db)
    if user:
        if user.password == password:
            return True
        else:
            return False
    else:
        return False

def sign_up(username,password,user_db):

    user=get_user(username,user_db)
    if not user:
        set_user(username,password,user_db)
        return True
    else:
        return False
        
    







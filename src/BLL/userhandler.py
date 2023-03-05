from Models import User

from DAL import connect
from DAL import add_data_user
from DAL import get_data_user



def sign_in(username,password):

    connection=connect()
    user=get_data_user(username,connection)
    if user:
        if user.password == password:
            return True
        else:
            return False
    else:
        return False

def sign_up(username,password):

    connection=connect()
    user=get_data_user(username,connection)
    if not user:
        user=User(username,password)
        add_data_user(user,connection)
        return True
    else:
        return False
        
    







from Models import User
from DAL import get_user
from DAL import set_user
from DAL import connect
from DAL import add_data_user



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

    connection=connect()
    #user=get_user(username,user_db)
    if True:
        user=User(username,password)
        #set_user(username,password,user_db)
        add_data_user(user,connection)
        return True
    else:
        return False
        
    







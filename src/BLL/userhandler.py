from Models import User
from DAL import get_user
from DAL import set_user



def sign_in(un,pw,db):

    user=get_user(db,un)
    if user:
        if user.password == pw:
            return True
        else:
            return False
    else:
        return False

def sign_up(usename,password,dbuser):

    set_user(usename,password,dbuser)
    print("welcom")







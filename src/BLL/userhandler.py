from Models import User
from DAL import get_user


def sign_in(un,pw,db):

    user=get_user(db,un)
    if user.password == pw:
        print("welcome")







import itertools
class User:
    count=0
    id_obj=itertools.count()
    def __init__(self,user_name,password):
        self.id=next(User.id_obj)
        self.user_name=user_name
        self.password=password

        User.count+=1
    
    def __del__(self):

        User.count-=1

        

    
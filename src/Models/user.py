import itertools
class User:
    count=0
    id_obj=itertools.count()
    def __init__(self,usar_name,password):
        self.id=next(User.id_obj)
        self.usar_name=usar_name
        self.password=password

        User.count+=1
    
    def __del__(self):

        User.count-=1

        

    
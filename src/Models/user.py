class User:
    count=0
    def __init__(self,user_name,password,id=0):
        self.id=id
        self.user_name=user_name
        self.password=password

        User.count+=1
    
    def __del__(self):

        User.count-=1

        

    
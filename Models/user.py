class User:
    count=0
    def __init__(self,first_name,last_name,password,email_address):
        self.first_name=first_name
        self.last_name=last_name
        self.password=password
        self.email_address=email_address

        User.count+=1

    
from Models import User
from DAL import seeder_userdb
from BLL import sign_in
def main():
    state=int(input("1.SignUp \n2.SignIn"))

    if(state==2):
        
        db=[]
        seeder_userdb(db)
        username=input("enter your username: ")
        password=input("enter your password: ")
        sign_in(username,password,db)




    

        


   
    
    

if __name__ == "__main__":
    main()
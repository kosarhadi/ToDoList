from Models import User
def main():
    state=int(input("1.SignUp \n2.SignIn"))
    if(state==1):
        fn=input("Enter Your First Name:")
        ln=input("Enter Your Last Name:")
        pa=input("Enter Your Password:")
        em=input("Enter Your Email Address:")

        U=User(fn,ln,pa,em)
        


   
    
    

if __name__ == "__main__":
    main()
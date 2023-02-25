from Models import User
from DAL import seeder_userdb
from DAL import seeder_taskdb
from BLL import sign_in
from BLL import sign_up
from BLL import show_task

def main():

    dbuser=[]
    seeder_userdb(dbuser)
    dbtask=[]
    seeder_taskdb(dbtask)
 
    while True:

        statelevel1=int(input("1.Signin \n2.Signup \n"))
        if(statelevel1 == 1):
            username=input("enter your username: ")
            password=input("enter your password: ")
            if sign_in(username,password,dbuser):

                statelevel2=int(input("1.show task\n"))
                if (statelevel2 == 1):
                    showlist=[]
                    showlist=show_task(dbuser,dbtask,username)
                    for i in showlist:
                        print(i)

        elif(statelevel1 == 2):
            username=input("enter your username: ")
            password=input("enter your password: ")
            sign_up(username,password,dbuser)


            






  
    
    

if __name__ == "__main__":
    main()
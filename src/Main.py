from Models import User
from DAL import seeder_userdb
from DAL import seeder_taskdb
from BLL import sign_in
from BLL import show_task

def main():

    statelevel1=int(input("1.Signin \n2.Signup \n"))
    if(statelevel1 == 1):
        dbuser=[]
        seeder_userdb(dbuser)
        username=input("enter your username: ")
        password=input("enter your password: ")
        sign_in(username,password,dbuser)

        statelevel2=int(input("1.show task\n"))
        if (statelevel2 == 1):
            dbtask=[]
            showlist=[]
            seeder_taskdb(dbtask)
            showlist=show_task(dbuser,dbtask,username)
            for i in showlist:
                print(i)

            






  
    
    

if __name__ == "__main__":
    main()
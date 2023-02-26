from DAL import seeder_userdb
from DAL import seeder_taskdb
from BLL import sign_in
from BLL import sign_up
from BLL import show_task
from BLL import create_task
from BLL import update_task
from BLL import delete_task

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

                statelevel2=int(input("1.show task\n2.create task\n"))
                if (statelevel2 == 1):
                    showlist=[]
                    showlist=show_task(dbuser,dbtask,username)
                    for i in showlist:
                        print(i)

                    statelevel3=int(input("1.update task\n2.delete task\n"))
                    if (statelevel3 == 1):
                        taskid=int(input("enter task number: "))
                        which_item=input("1.title\ 2.status\ 3.data ")
                        change_text=input("enter your change text: ")
                        showlist=[]
                        showlist=show_task(dbuser,dbtask,username)
                        update_success=False
                        for i in showlist:
                            if i.id == taskid:
                                update_task(change_text,which_item,taskid,dbtask)
                                print("update done")
                                update_success=True
                        if not update_success:
                            print("task number wrong") 
                        

                    elif (statelevel3 == 2):
                        taskid=int(input("enter task number: "))
                        showlist=[]
                        showlist=show_task(dbuser,dbtask,username)
                        delete_success=False
                        for i in showlist:
                            if i.id == taskid:
                                delete_task(taskid,dbtask)
                                print("delete done")
                                delete_success=True
                        if not delete_success:
                            print("task number wrong")

                        
                elif (statelevel2 == 2):
                    title=input("enter title: ")
                    status=input("enter status (to do\in progress\done): ")
                    date=input("enter date: ")
                    create_task(title,status,date,dbtask,username,dbuser)
                    showlist=[]
                    showlist=show_task(dbuser,dbtask,username)
                    for i in showlist:
                        print(i)

                    statelevel3=int(input("1.update task\n2.delete task\n"))
                    if (statelevel3 == 1):
                        taskid=int(input("enter task number: "))
                        which_item=input("1.title\ 2.status\ 3.data ")
                        change_text=input("enter your change text: ")
                        showlist=[]
                        showlist=show_task(dbuser,dbtask,username)
                        update_success=False
                        for i in showlist:
                            if i.id == taskid:
                                update_task(change_text,which_item,taskid,dbtask)
                                print("update done")
                                update_success=True
                        if not update_success:
                            print("task number wrong") 
                        

                    elif (statelevel3 == 2):
                        taskid=int(input("enter task number: "))
                        showlist=[]
                        showlist=show_task(dbuser,dbtask,username)
                        delete_success=False
                        for i in showlist:
                            if i.id == taskid:
                                delete_task(taskid,dbtask)
                                print("delete done")
                                delete_success=True
                        if not delete_success:
                            print("task number wrong")


            else:
                print("username or password wrong")

        elif(statelevel1 == 2):
            username=input("enter your username: ")
            password=input("enter your password: ")
            if sign_up(username,password,dbuser):

                statelevel2=int(input("1.show task\n2.create task\n"))
                if (statelevel2 == 1):
                    showlist=[]
                    showlist=show_task(dbuser,dbtask,username)
                    for i in showlist:
                        print(i)

                    statelevel3=int(input("1.update task\n2.delete task\n"))
                    if (statelevel3 == 1):
                        taskid=int(input("enter task number: "))
                        which_item=input("1.title\ 2.status\ 3.data ")
                        change_text=input("enter your change text: ")
                        showlist=[]
                        showlist=show_task(dbuser,dbtask,username)
                        update_success=False
                        for i in showlist:
                            if i.id == taskid:
                                update_task(change_text,which_item,taskid,dbtask)
                                print("update done")
                                update_success=True
                        if not update_success:
                            print("task number wrong") 
                        

                    elif (statelevel3 == 2):
                        taskid=int(input("enter task number: "))
                        showlist=[]
                        showlist=show_task(dbuser,dbtask,username)
                        delete_success=False
                        for i in showlist:
                            if i.id == taskid:
                                delete_task(taskid,dbtask)
                                print("delete done")
                                delete_success=True
                        if not delete_success:
                            print("task number wrong")

                        
                elif (statelevel2 == 2):
                    title=input("enter title: ")
                    status=input("enter status (to do\in progress\done): ")
                    date=input("enter date: ")
                    create_task(title,status,date,dbtask,username,dbuser)
                    showlist=[]
                    showlist=show_task(dbuser,dbtask,username)
                    for i in showlist:
                        print(i)

                    statelevel3=int(input("1.update task\n2.delete task\n"))
                    if (statelevel3 == 1):
                        taskid=int(input("enter task number: "))
                        which_item=input("1.title\ 2.status\ 3.data ")
                        change_text=input("enter your change text: ")
                        showlist=[]
                        showlist=show_task(dbuser,dbtask,username)
                        update_success=False
                        for i in showlist:
                            if i.id == taskid:
                                update_task(change_text,which_item,taskid,dbtask)
                                print("update done")
                                update_success=True
                        if not update_success:
                            print("task number wrong") 
                        

                    elif (statelevel3 == 2):
                        taskid=int(input("enter task number: "))
                        showlist=[]
                        showlist=show_task(dbuser,dbtask,username)
                        delete_success=False
                        for i in showlist:
                            if i.id == taskid:
                                delete_task(taskid,dbtask)
                                print("delete done")
                                delete_success=True
                        if not delete_success:
                            print("task number wrong")
            




    

    

if __name__ == "__main__":
    main()
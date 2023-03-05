from BLL import sign_in
from BLL import sign_up

from BLL import show_task
from BLL import create_task
from BLL import update_task
from BLL import delete_task

def main():

    while True:

        statelevel1=int(input("1.Signin \n2.Signup \n"))
        if(statelevel1 == 1):
            username=input("enter your username: ")
            password=input("enter your password: ")
            if sign_in(username,password):

                print("welcom",username)
                statelevel2=int(input("1.show task\n2.create task\n"))
                if (statelevel2 == 1):
                    showlist=[]
                    showlist=show_task(username)
                    for i in showlist:
                        print(i)

                    statelevel3=int(input("1.update task\n2.delete task\n"))
                    if (statelevel3 == 1):
                        taskid=int(input("enter task number: "))
                        which_item=input("1.title\ 2.status\ 3.data ")
                        change_text=input("enter your change text: ")
                        showlist=[]
                        showlist=show_task(username)
                        update_success=False
                        for i in showlist:
                            if i.id == taskid:
                                update_task(change_text,which_item,taskid)
                                print("update done")
                                update_success=True
                        if not update_success:
                            print("task number wrong") 
                        

                    elif (statelevel3 == 2):
                        taskid=int(input("enter task number: "))
                        showlist=[]
                        showlist=show_task(username)
                        delete_success=False
                        for i in showlist:
                            if i.id == taskid:
                                delete_task(taskid)
                                print("delete done")
                                delete_success=True
                        if not delete_success:
                            print("task number wrong")

                        
                elif (statelevel2 == 2):
                    title=input("enter title: ")
                    status=input("enter status (to do\done): ")
                    date=input("enter date: ")
                    create_task(title,status,date,username)
                    showlist=[]
                    showlist=show_task(username)
                    for i in showlist:
                        print(i)

                    statelevel3=int(input("1.update task\n2.delete task\n"))
                    if (statelevel3 == 1):
                        taskid=int(input("enter task number: "))
                        which_item=input("1.title\ 2.status\ 3.data ")
                        change_text=input("enter your change text: ")
                        showlist=[]
                        showlist=show_task(username)
                        update_success=False
                        for i in showlist:
                            if i.id == taskid:
                                update_task(change_text,which_item,taskid)
                                print("update done")
                                update_success=True
                        if not update_success:
                            print("task number wrong") 
                        

                    elif (statelevel3 == 2):
                        taskid=int(input("enter task number: "))
                        showlist=[]
                        showlist=show_task(username)
                        delete_success=False
                        for i in showlist:
                            if i.id == taskid:
                                delete_task(taskid)
                                print("delete done")
                                delete_success=True
                        if not delete_success:
                            print("task number wrong")


            else:
                print("username or password wrong")

        elif(statelevel1 == 2):
            username=input("enter your username: ")
            password=input("enter your password: ")
            if sign_up(username,password):

                statelevel2=int(input("1.show task\n2.create task\n"))
                if (statelevel2 == 1):
                    showlist=[]
                    showlist=show_task(username)
                    for i in showlist:
                        print(i)

                    statelevel3=int(input("1.update task\n2.delete task\n"))
                    if (statelevel3 == 1):
                        taskid=int(input("enter task number: "))
                        which_item=input("1.title\ 2.status\ 3.data ")
                        change_text=input("enter your change text: ")
                        showlist=[]
                        showlist=show_task(username)
                        update_success=False
                        for i in showlist:
                            if i.id == taskid:
                                update_task(change_text,which_item,taskid)
                                print("update done")
                                update_success=True
                        if not update_success:
                            print("task number wrong") 
                        

                    elif (statelevel3 == 2):
                        taskid=int(input("enter task number: "))
                        showlist=[]
                        showlist=show_task(username)
                        delete_success=False
                        for i in showlist:
                            if i.id == taskid:
                                delete_task(taskid)
                                print("delete done")
                                delete_success=True
                        if not delete_success:
                            print("task number wrong")

                        
                elif (statelevel2 == 2):
                    title=input("enter title: ")
                    status=input("enter status (to do\done): ")
                    date=input("enter date: ")
                    create_task(title,status,date,username)
                    showlist=[]
                    showlist=show_task(username)
                    for i in showlist:
                        print(i)

                    statelevel3=int(input("1.update task\n2.delete task\n"))
                    if (statelevel3 == 1):
                        taskid=int(input("enter task number: "))
                        which_item=input("1.title\ 2.status\ 3.data ")
                        change_text=input("enter your change text: ")
                        showlist=[]
                        showlist=show_task(username)
                        update_success=False
                        for i in showlist:
                            if i.id == taskid:
                                update_task(change_text,which_item,taskid,)
                                print("update done")
                                update_success=True
                        if not update_success:
                            print("task number wrong") 
                        

                    elif (statelevel3 == 2):
                        taskid=int(input("enter task number: "))
                        showlist=[]
                        showlist=show_task(username)
                        delete_success=False
                        for i in showlist:
                            if i.id == taskid:
                                delete_task(taskid)
                                print("delete done")
                                delete_success=True
                        if not delete_success:
                            print("task number wrong")
            




    

    

if __name__ == "__main__":
    main()
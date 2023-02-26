from Models import User
from Models import Task


def seeder_userdb(db):

    U1=User('kosar','1273')
    db.append(U1)

    U2=User('habib','6859')
    db.append(U2)

    U3=User('fatemeh','1379')
    db.append(U3)

    U4=User('user','1111')
    db.append(U4)

    U5=User('admin','0000')
    db.append(U5)

def get_user(username,user_db):

    for i in user_db:
        if i.user_name == username:
            return i
                      
def set_user(username,password,user_db):
    
    U=User(username,password)
    user_db.append(U)



def seeder_taskdb(db):

    T1=Task('create todo list','in progress','12/10',0)
    db.append(T1)

    T2=Task('read book','to do','12/11',0)
    db.append(T2)

    T3=Task('Training','in progress','01/30',1)
    db.append(T3)

    T4=Task('check list','to do','01/30',4)
    db.append(T4)

def get_user_tasks(userid,task_db):

    showlist=[]
    for i in task_db:
        if i.userid == userid:
            showlist.append(i)
    return showlist

def set_change_task(change_text,which_item,taskid,task_db):
     
     which_item=int(which_item)

     for i in task_db:
        if i.id == taskid:
            if which_item == 1:
                i.title = change_text
            elif which_item == 2:
                i.status = change_text
            elif which_item == 3:
                i.date = change_text
            
def set_task(title,status,date,task_db,userid):
    
    T=Task(title,status,date,userid)
    task_db.append(T)

def delete(taskid,task_db):

    for i in task_db:
        if i.id == taskid:
            task_db.remove(i)

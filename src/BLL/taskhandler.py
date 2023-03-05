from Models import Task
from DAL import update_data_task
from DAL import connect

from DAL import get_data_user

from DAL import add_data_task
from DAL import get_data_task
from DAL import delete_data_task


def show_task(username):

    connection=connect()
    user=get_data_user(username,connection)
    tasks=get_data_task(user.id,connection)
    connection.close()
    return tasks

def create_task(title,status,date,username):

    connection=connect()
    user=get_data_user(username,connection)
    task=Task(title,status,date,user.id)
    add_data_task(task,connection)
    connection.close()
    
def update_task(change_text,which_item,taskid):

    connection=connect()
    update=update_data_task(change_text,which_item,taskid,connection)
    connection.close()
    return update

def delete_task(taskid):

    connection=connect()
    delete_data_task(taskid,connection)
    connection.close()

    


    

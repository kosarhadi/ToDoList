from DAL import get_user_tasks
from DAL import set_change_task
from DAL import set_task
from DAL import delete

from DAL import get_user

def show_task(user_db,task_db,username):

    user=get_user(username,user_db)
    return get_user_tasks(user.id,task_db)

def create_task(title,status,date,task_db,username,user_db):

    user=get_user(username,user_db)
    set_task(title,status,date,task_db,user.id)

def update_task(change_text,which_item,taskid,task_db):

    return set_change_task(change_text,which_item,taskid,task_db)

def delete_task(taskid,task_db):

    delete(taskid,task_db)

    


    

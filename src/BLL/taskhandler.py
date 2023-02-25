from Models import Task

from DAL import get_task
from DAL import get_user

def show_task(dbu,dbt,un):

    user=get_user(dbu,un)
    
    return get_task(dbt,user.id)

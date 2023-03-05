from DAL import connect
from DAL import create_table_user
from DAL import create_table_task

connection=connect()
create_table_user(connection)
create_table_task(connection)

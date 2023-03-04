from DAL import connect
from DAL import create_table_user

connection=connect()
create_table_user(connection)

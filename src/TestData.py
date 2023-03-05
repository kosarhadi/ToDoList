from DAL import connect
from DAL import seeder_db_user
from DAL import seeder_db_task

connection=connect()
seeder_db_user(connection)
seeder_db_task(connection)



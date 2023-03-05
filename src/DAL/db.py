from Models import User
from Models import Task

import mysql.connector as database

def connect():
    connection = database.connect(
        user="root",
        password="1@admin",
        host="127.0.0.1",
        database="db_ToDoList")
    return connection


def create_table_user(connection):
    cursor = connection.cursor()
    try:
        statement = "CREATE TABLE user (id INT AUTO_INCREMENT, username VARCHAR(50), password VARCHAR(50), PRIMARY KEY(id))"
        cursor.execute(statement)
        connection.commit()
        print("Successfully create table user")
    except database.Error as e:
        print(f"Error create table: {e}")
    cursor.close()

def seeder_db_user(connection):

    cursor = connection.cursor()
    try:
        statement = "INSERT INTO user (username,password) VALUES (%s, %s)"
        data = [
                ('kosar','1273'),
                ('habib','1234'),
                ('fatemeh','5678'),
                ('user','0000'),
                ('admin','0000')
                ]
        cursor.executemany(statement, data)
        connection.commit()
        print(cursor.rowcount,"Record inserted Successfully added into user table")
    except database.Error as e:
        print(f"Error adding entry to database: {e}")
    cursor.close()

def add_data_user(user,connection):
    cursor = connection.cursor()
    try:
        statement = "INSERT INTO user (username,password) VALUES (%s, %s)"
        data = (user.user_name,user.password)
        cursor.execute(statement, data)
        connection.commit()
        print("Successfully added entry to user table")
    except database.Error as e:
        print(f"Error adding entry to user table: {e}")
    cursor.close()

def get_data_user(username,connection):
    cursor = connection.cursor()
    try:
      statement = "SELECT id ,username ,password FROM user WHERE username=%s"
      data = (username,)
      cursor.execute(statement, data)
      result = cursor.fetchone()
      user=User(result[1],result[2],result[0])
      return user
    except database.Error as e:
      print(f"Error retrieving entry from database: {e}")
    cursor.close()

    
def create_table_task(connection):
    cursor = connection.cursor()
    try:
        statement = "CREATE TABLE task (id INT AUTO_INCREMENT, title VARCHAR(50), status ENUM('todo','done'), date VARCHAR(50), user_id INT, PRIMARY KEY(id))"
        cursor.execute(statement)
        connection.commit()
        print("Successfully create table task")
    except database.Error as e:
        print(f"Error create table: {e}")
    cursor.close()

def seeder_db_task(connection):

    cursor = connection.cursor()
    try:
        statement = "INSERT INTO task (title,status,date,user_id) VALUES (%s, %s, %s, %s)"
        data = [
                ('create todolist api','todo','12/24',1),
                ('create db','done','12/12',1),
                ('travel','todo','12/18',2),
                ('nothing','todo','12/29',3),
                ('say welcom','done','12/01',4)
                ]
        cursor.executemany(statement, data)
        connection.commit()
        print(cursor.rowcount,"Record inserted Successfully added into task table")
    except database.Error as e:
        print(f"Error adding entry to database: {e}")
    cursor.close()

def add_data_task(task,connection):
    cursor = connection.cursor()
    try:
        statement = "INSERT INTO task (title,status,date,user_id) VALUES (%s, %s, %s, %s)"
        data = (task.title,task.status,task.date,task.userid)
        cursor.execute(statement, data)
        connection.commit()
        print("Successfully added entry to task table")
    except database.Error as e:
        print(f"Error adding entry to task table: {e}")
    cursor.close()

def get_data_task(userid,connection):

    cursor = connection.cursor()
    try:
      statement = "SELECT id ,title ,status ,date ,user_id FROM task WHERE user_id=%s"
      data = (userid,)
      cursor.execute(statement, data)
      result = cursor.fetchall()
      cursor.close()
      returnlist=[]
      for i in result:
          task=Task(i[1],i[2],i[3],i[4],i[0])
          returnlist.append(task)
      return returnlist
    except database.Error as e:
      print(f"Error retrieving entry from database: {e}")
    cursor.close()

def update_data_task(change_text,which_item,taskid,connection):
    cursor = connection.cursor()

    try:
        which_item=int(which_item)
        if which_item == 1:
            statement = "UPDATE task SET title = (%s) WHERE id = (%s)"
            data = (change_text,taskid)

        elif which_item == 2:
            statement = "UPDATE task SET status = (%s) WHERE id = (%s)"
            data = (change_text,taskid)    
        elif which_item == 3:
            statement = "UPDATE task SET date = (%s) WHERE id = (%s)"
            data = (change_text,taskid)     
        cursor.execute(statement, data)
        connection.commit()
        print("Successfully updated task table")
    except database.Error as e:
        print(f"Error in updating task table: {e}")
    cursor.close()
     
def delete_data_task(taskid,connection):

    cursor = connection.cursor()
    try:
        statement = "DELETE FROM task WHERE id=(%s)"
        data = (taskid,)
        cursor.execute(statement, data)
        connection.commit()
        print("Successfully delete entry to task table")
    except database.Error as e:
        print(f"Error deleting entry to task table: {e}")
    cursor.close()

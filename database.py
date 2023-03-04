import os
import mysql.connector as database

connection = database.connect(
    user="root",
    password="1@admin",
    host="127.0.0.1",
    database="db_ToDoList")
cursor = connection.cursor()

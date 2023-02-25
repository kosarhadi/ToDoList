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

    return db


def seeder_taskdb(db):

    T1=Task('creat todo list','in progress','12/10',0)
    db.append(T1)

    T2=Task('read book','to do','12/11',0)
    db.append(T2)

    T3=Task('Training','in progress','01/30',1)
    db.append(T3)

    T4=Task('check list','to do','01/30',4)
    db.append(T4)

    return db




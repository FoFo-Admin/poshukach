import json
import requests
import mysql.connector

#########################################
def sendToServer(sql):
    DataBase = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="",
    charset='utf8'
    )

    Cursor = DataBase.cursor()
    Cursor.execute(sql)

    DataBase.commit()
    DataBase.close()


def getFromServer(sql):
    DataBase = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="",
    charset='utf8'
    )
    Cursor = DataBase.cursor()
    
    Cursor.execute(sql)
    result = Cursor.fetchall()

    DataBase.close()

    return result
#########################################

import mysql.connector

def connection():

        conn = mysql.connector.connect(
        db='mover',
        user='root',
        passwd='',
        host='localhost')

        return conn
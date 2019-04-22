import mysql.connector
import time

def test_can_connect(mysqld):
    con = mysql.connector.connect(
            host="127.0.0.1",
            database="snippet",
            user="snippet",
            password="snippet")
    assert con.is_connected() == True

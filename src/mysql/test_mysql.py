import mysql.connector

def run():
    try:
        con = mysql.connector.connect(
                host="127.0.0.1",
                database="snippet",
                user="snippet",
                password="snippet")
        if con.is_connected():
            print("Connected to MySQL database")
    except Error as e:
        print(e)
    finally:
        con.close()

if __name__ == '__main__':
    run()

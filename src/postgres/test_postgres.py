import psycopg2

def run():
    try:
        con = psycopg2.connect(
                user="snippet",
                password="snippet",
                host="127.0.0.1",
                port="5432",
                database="snippet")
        cursor = con.cursor()
        print(con.get_dsn_parameters(), "\n")
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to {version}".format(version=record))
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to Postgres", error)
    finally:
        if(con):
            cursor.close()
            con.close()

if __name__ == '__main__':
    run()

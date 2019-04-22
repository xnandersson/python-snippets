import sqlite3

def run():
#    con = sqlite3.connect(":memory:")
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    try:
        cur.execute("create table users (user varchar(64), password varchar(64))")
    except sqlite3.OperationalError as e:
        print("Warning: " + str(e))
    cur.execute("insert into users (user, password) values('Niklas','Mypassword')")
    cur.execute("insert into users (user, password) values(?,?)", ('Niklas2', 'Password2'))
    cur.execute("insert into users (user, password) values(:name,:password)", {'name': 'Niklas3', 'password': 'Password3'})

    con.commit()
    rs = cur.execute("select user,password from users")
    for user in rs:
        print("{user} {password}".format(
                    user=user[0],
                    password=user[1]))
    cur.close()
    con.close()

if __name__ == '__main__':
    run()

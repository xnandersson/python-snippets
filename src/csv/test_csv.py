import csv


def create_csv():
    with open('data.csv', 'w') as f:
        f.write("user,password\n")
        f.write("user1,password1\n")
        f.write("user2,password2\n")
   
def read_csv():
    reader = csv.DictReader(open('data.csv'))
    for row in reader:
        print("{user} {password}".format(user=row["user"], password=row["password"]))

if __name__ == '__main__':
    create_csv()
    read_csv()

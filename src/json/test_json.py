import json


def create_json():
    data = [
        {
            "user": "Niklas Andersson",
            "password": "mypassword"
        },
        {
            "user": "John Döe",
            "password": "hispassword"
        }
    ]
    with open('data.json', 'w') as f:
        f.write(json.dumps(data))


def read_json():
    data = json.loads(open('data.json').read())
    print(data)

if __name__ == '__main__':
    create_json()
    read_json()

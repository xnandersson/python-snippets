from xml.etree import ElementTree

def run():
    data = ElementTree.parse('data.xml')
    root = data.getroot()

    for p in root.findall('.//users/user'):
        print("Name: {name}".format(
                    name=p.find('name').text))

if __name__ == '__main__':
    run()

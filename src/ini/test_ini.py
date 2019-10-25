from configparser import ConfigParser

parser = ConfigParser()
parser.read([
    os.path.join(os.path.expanduser("~"),'snippets.ini'),
    '/etc/python-snippets/snippets.ini',
    '/etc/python-snippets.ini',
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'conf', 'snippets.ini')
])

""" 
>>> help(parser) # Gives you documentation for parser
    """
print(parser.get('mongo', 'mongo_uri'))

print(parser.has_section('django'))
print(parser.has_section('django2'))
print(parser.has_option('django', 'database'))

for option in parser.options('user'):
    print(option)

for key,value in parser.items('user'):
    print("{key} {value}".format(key=key, value=value))

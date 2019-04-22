from configparser import ConfigParser

parser = ConfigParser()
parser.read('snippet.ini')

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

import yaml
import pprint

""" https://pyyaml.org/wiki/PyYAMLDocumentation """

def run():
    print("Running")
    data = yaml.load(open('data.yaml'), Loader=yaml.Loader)
    pprint.pprint(data)

if __name__ == '__main__':
    run()

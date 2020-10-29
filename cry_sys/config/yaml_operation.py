import yaml


class YamlOperation:

    def __init__(self,localhost_file):
        with open(localhost_file) as yaml_file:
            self.data = yaml.load(yaml_file,yaml.FullLoader)

    def get_locator(self,page,local):
        return self.data[page][local]
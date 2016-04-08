import yaml


class ConfigLoad:
    def __init__(self):
        self.config_path = '../config/config.yml'

    def load_config(self):
        try:
            with open(self.config_path, 'r') as config:
                data = yaml.load(config)
            return data
        except Exception as e:
            print "Config load failed... : ", e

    def print_config(self):
        print self.load_config()


if __name__ == '__main__':
    c = ConfigLoad()
    c.print_config()
import yaml


class ConfigLoad:
    def __init__(self):
        self.config_path = '../config/config.yml'
        self.config = self.load_config()
    def load_config(self):
        try:
            with open(self.config_path, 'r') as config:
                data = yaml.load(config)
            return data
        except Exception as e:
            print "Config load failed... : ", e

    def print_config(self):
        print self.load_config()

    def get_pins(self):
       return  self.config['grovepi_config']['pins']

    def get_threshold(self):
       return self.config['grovepi_config']['threshold']

    #sound sensor pin
    def get_ss_pin(self):
       return self.get_pins['sound_sensor']
    #red led pin
    def get_rled_pin(self):
       return self.get_pins['red_led']
    #rgb display pin
    def get_rgb_pin(self):
       return self.get_pins['rbg_display']
    #ultrasonic range finder pin
    def get_usonic_pin(self):
       return self.get_pins['ultrasonic_pin']


if __name__ == '__main__':
    c = ConfigLoad()
    c.get_pins()

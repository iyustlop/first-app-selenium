from configparser import ConfigParser


class MyUser:

    def __init__(self):
        self.parser = ConfigParser()
        self.parser.read('example.ini')

    def user(self):
        return self.parser.get('login', 'email')

    def password(self):
        return self.parser.get('login', 'psw')

    def driver(self):
        return self.parser.get('login', 'driver')

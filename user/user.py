from configparser import ConfigParser


class MyUser:

    def __init__(self):
        self.parser = ConfigParser()
        self.parser.read('example.ini')

    def user(self):
        return self.parser.get("DEFAULT", 'email')

    def password(self):
        return self.parser.get("DEFAULT", 'psw')

    def driver(self):
        return self.parser.get('DEFAULT', 'driver')

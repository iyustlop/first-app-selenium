import os
from configparser import ConfigParser


class MyUser:

    def __init__(self):
        self.parser = ConfigParser()
        self.parser.read('/home/sobremesa/Documentos/first-app-selenium/user/example.cfg')

    def user(self):
        return self.parser.get('DEFAULT', 'email')

    def password(self):
        return self.parser.get('DEFAULT', 'psw')

    def driver(self):
        return self.parser.get('DEFAULT', 'driver')



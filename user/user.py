import os
from configparser import ConfigParser

class myUser:

    def __init__(self):
        self.parser = ConfigParser()
        self.parser.read('/home/sobremesa/Documentos/first-app-selenium/user/example.cfg')

    def getUser(self):
        return self.parser.get('DEFAULT', 'email')

    def getPassword(self):
        return self.parser.get('DEFAULT', 'psw')

    def getDriver(self):
        return self.parser.get('DEFAULT', 'driver')



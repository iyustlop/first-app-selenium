import os
from configparser import ConfigParser,RawConfigParser

class myUser:

    def getUser(self):
        parser = ConfigParser()
        parser.read('/home/sobremesa/Documentos/first-app-selenium/user/example.cfg')
        return parser.get('DEFAULT', 'email')

    def getPassword(self):
        parser = ConfigParser()
        parser.read('/home/sobremesa/Documentos/first-app-selenium/user/example.cfg')
        return parser.get('DEFAULT', 'psw')

    def getDriver(self):
        parser = ConfigParser()
        parser.read('/home/sobremesa/Documentos/first-app-selenium/user/example.cfg')
        return parser.get('DEFAULT', 'driver')



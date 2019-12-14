import configparser

class DbConfigReader:
    def __init__(self, fileName):
        self.file = configparser.ConfigParser()
        self.file.read(fileName)


    def retrieveConnectionSetting(self):
        section = self.file['DbConfig']
        dbConfigs = {
            'host' : section['host'],
            'user' : section['user'],
            'password' : section['password'],
            'db' : section['db'],
            'charset' : section['charset'],
            'cursorclass' : section['cursorclass']
        }


        return dbConfigs
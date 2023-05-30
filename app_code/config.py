from configparser import ConfigParser

class AppConfig(object):

    _theConfigParser = None

    def __init__(self,config_file_path):
        self._theConfigParser = ConfigParser()
        self.readCfg(config_file_path)

    def readCfg(self,config_file_path):
        print(self._theConfigParser.read(config_file_path))

        print("config sections are: ", self._theConfigParser.sections())
        print("username:", self._theConfigParser.get('debug', 'user_name'))
        print("port: ", self._theConfigParser.getint('server', 'port'))

    def getStringValue(self,category,name):
        return self._theConfigParser.get(category, name)

    def getIntValue(self,category,name):
        return self._theConfigParser.getint(category, name)
    def getBoolValue(self,category,name):
        return self._theConfigParser.getboolean(category, name)
    def isUsingDebugValues(self):
        return self._theConfigParser.getboolean('debug', 'use_debug_values')

    def getUserName(self):
        return self._theConfigParser.get('debug', 'user_name')
    def getPassword(self):
        return self._theConfigParser.get('debug', 'user_password')
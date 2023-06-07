import configparser

def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Config.cfg") #single dot for calling this from other files double dot for calling it from here
    return config.get(section,key)

def readElementData(section,key):
    config=configparser.ConfigParser()
    config.read("./ConfigurationFiles/Elements.cfg")
    return config.get(section,key)


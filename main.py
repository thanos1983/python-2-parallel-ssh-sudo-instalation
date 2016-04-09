import os
import ConfigParser
import pprint

Config = ConfigParser.ConfigParser()
config_path = os.path.dirname(os.path.abspath(__file__))
print config_path

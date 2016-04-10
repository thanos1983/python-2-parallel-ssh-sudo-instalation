#!/usr/bin/python

import ConfigParser


class ConfigurationFileProcess(object):
    """Class processing configuration file.
        Load all hosts data that we want to probe"""

    def process_conf_file(self, conf_file):
        """
        :rtype: Dictionary containing data for each host, extracted from configuration file
        """
        config = ConfigParser.ConfigParser()
        config.read(conf_file)

        dictionary = {}
        for section_name in config.sections():
            dictionary[section_name] = config.items(section_name)
        return dictionary

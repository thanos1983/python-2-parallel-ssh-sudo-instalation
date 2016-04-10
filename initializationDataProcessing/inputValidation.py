#!/usr/bin/python
import sys

class InputValidation(object):

    def input_validation(self):
        if len(sys.argv) != 2:
            print "Usage: python {} [Configuration File]".format(sys.argv[0])
            sys.exit(1)
        elif not sys.argv[1].endswith('.cfg') and not sys.argv[1].endswith('.ini'):
            print "Usage: python {} [Configuration File.ini or Configuration File.cfg]".format(sys.argv[0],
                                                                                               sys.argv[1])
            sys.exit(1)

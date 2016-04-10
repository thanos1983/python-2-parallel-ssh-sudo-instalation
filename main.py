import os
import sys
import pprint
import ConfigParser
from initializationDataProcessing import inputValidation

from pssh.pssh_client import ParallelSSHClient
from pssh.exceptions import AuthenticationException, UnknownHostException, ConnectionErrorException

if __name__ == '__main__':
    user_input = sys.argv
    input_obj = inputValidation.InputValidation()
    input_obj.input_validation()
    exit(0)


    conf_file = sys.argv[1]

    pprint.pprint(extract_conf_data(config.sections()))
    exit(0)
    pprint.pprint(config.options(config.sections()[0]))
    pprint.pprint(config.items(config.sections()[0]))
    pprint.pprint()
    exit(0)

    client = ParallelSSHClient(config.sections(), user='root')
    try:
        output = client.run_command('ls -la', sudo=True, stop_on_errors=False)
        pprint(output)
        exit(0)
    except(AuthenticationException, UnknownHostException, ConnectionErrorException) as e:
        print e
        exit(1)
import sys
import pprint
from initializationDataProcessing import inputValidation, configurationFileProcess

from pssh.pssh_client import ParallelSSHClient
from pssh.exceptions import AuthenticationException, UnknownHostException, ConnectionErrorException

if __name__ == '__main__':

    # check user input
    inputValidation.InputValidation().input_validation()

    # instantiate configuration file process obj
    configurationFileProcess_obj = configurationFileProcess.ConfigurationFileProcess()
    pprint.pprint(configurationFileProcess_obj.process_conf_file(sys.argv[1]))
    exit(0)

    client = ParallelSSHClient('host', user='root')
    try:
        output = client.run_command('ls -la', sudo=True, stop_on_errors=False)
        pprint.pprint(output)
        exit(0)
    except(AuthenticationException, UnknownHostException, ConnectionErrorException) as e:
        print e
        exit(1)
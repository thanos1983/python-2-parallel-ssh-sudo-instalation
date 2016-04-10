import pprint
import pssh.utils
from initializationDataProcessing import inputValidation, configurationFileProcess

from pssh.pssh_client import ParallelSSHClient
from pssh.exceptions import AuthenticationException, UnknownHostException, ConnectionErrorException

if __name__ == '__main__':

    # check user input
    inputValidation.InputValidation().input_validation()

    # instantiate configuration file process obj
    configurationFileProcess_obj = configurationFileProcess.ConfigurationFileProcess()
    #pprint.pprint(configurationFileProcess_obj.process_conf_file(sys.argv[1]))

    client = ParallelSSHClient(['127.0.0.1'], user='tinyos', password='K@potes1983', port=19013)
    try:
        output = client.run_command('ls -ltrh /home/tinyos', sudo=True, stop_on_errors=False)
        test = client.get_output()
        pprint.pprint(output)
        for host in output:
            for line in output[host]['stdout']:
                print line
        pprint.pprint(test)
        del client
        exit(0)
    except(AuthenticationException, UnknownHostException, ConnectionErrorException) as e:
        print e
        exit(1)
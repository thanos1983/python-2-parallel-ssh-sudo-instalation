# python-2-parallel-ssh-sudo-instalation
Install into multiple UnixOS packages in parallel through SSH

Necessary components:
pip install parallel-ssh

Necessary file to have is a configuration file, with extension '.ini' or '.cfg'
Sample of file provided bellow:

[hostname or IP]
port    : port number
user    : user name
password: password

[hostname 2 or IP]
port    : port number
user    : user name
password: password

.   .   .
.   .   .
.   .   .

[hostname n or IP]
port    : port number
user    : user name
password: password

import socket
import argparse  # https://docs.python.org/3/howto/argparse.html
import os

from datetime import datetime

parser = argparse.ArgumentParser(description='utility for connection testing')
parser.add_argument(
    'connection_type',
    default='client',
    choices=['client', 'server'],
    help='run in either client or server mode'
)
# server name or ip
parser.add_argument(
    '-s',
    '--server',
    default='127.0.0.1',
    help='provide server name or IP address'
)

# server port
parser.add_argument(
    '-p',
    '--port',
    type=int,
    default='9000',
    help='provide server port number'
)

# client needs targeted server name or ip
my_parameters = parser.parse_args()
server_port = str(my_parameters.port)
print("mode: " + my_parameters.connection_type + " for " + my_parameters.server + " on port " + server_port)
timestamp = datetime.now().strftime('%Y-%m%d-%H%M-%S')
print("current time: " + timestamp)
print("PID of this script is: " + str(os.getpid()))

if my_parameters.connection_type in ['client']:
    print("client mode: " + my_parameters.connection_type + " for " + my_parameters.server + " on port " + server_port)
    s = socket.socket()
    client = (my_parameters.server, my_parameters.port)
    s.connect(client)
    print(s.recv(1024))
    s.close()
elif my_parameters.connection_type in ['server']:
    #print("PID of this script is: " + str(os.getpid()))
    print("server mode: " + my_parameters.connection_type + " for " + my_parameters.server + " on port " + server_port)
    s = socket.socket()
    print("socket created successfully")
    server = (my_parameters.server, my_parameters.port)
    s.bind(server)
    print(my_parameters.server + " using port " + str(my_parameters.port))
    s.listen(4)
    print(my_parameters.server + " listening")
    while True:
        connection, address = s.accept()
        print("connection from " + address)
        message = "connected with " + my_parameters.server + " on port " + my_parameters.port
        connection.sendall(message)
        connection.close()
else:
    print("error: " + my_parameters.connection_type + " message should have been prevented by choice in argparse")

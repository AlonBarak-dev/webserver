# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
HOST = "0.0.0.0"
PORT = 6789

serverSocket.bind((HOST, PORT))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        # outputdata = connectionSocket.recv(1024)
        # Send one HTTP header line into socket
        outputdata = []
        outputdata.append('HTTP/1.1 200 OK\n\n')
        outputdata.append(f.read())
        # connectionSocket.sendall(outputdata.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError as err:
        print("file not found: ", err)
    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

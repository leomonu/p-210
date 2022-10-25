import socket
from threading import Thread
import time
import os
from pyftpdlib.authorizers import DummyAuthorizer 
from pyftpdlib.handlers import FTPHandler 
from pyftpdlib.servers import FTPServer


IP_ADDRESS = '127.0.0.1'
PORT = 8080
SERVER = None
clients = {}


def acceptConnections():
    global SERVER
    global clients

    while True:
        client, addr = SERVER.accept()
        client_name = client.recv(4096).decode().lower()
        clients[client_name] = {
            "client": client,
            "address": addr,
            "connected_with": "",
            "file_name": "",
            "flie_size": 4096
        }
        print(f"Connections established with {client_name}:{addr}")

        thread = Thread(target=handleClient, args=(client, client_name,))
        thread.start()


def setup():
    print("\n\t\t\t\t\t\tIP Music\n")

    # Getting global values
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(100)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    acceptConnections()

# def ftp():
#     global ip_address
#     authorizer = DummyAuthorizer()
#     authorizer.add_user("lftpd", "lftpd", ".", perm="elradfmw")
#     handler = FTPHandler
#     handler.authorizer = authorizer
#     ftp_server = FTPServer((ip_address, 21), handler)
#     ftp_server.serve_forever()


setup_thread = Thread(target=setup)
setup_thread.start()

# ftp_thread = Thread(target=ftp)
# ftp_thread.start()

import socket
from cryptography.fernet import Fernet

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 9999))
    key = client_socket.recv(1024)
    c = Fernet(key)

    while True:
        message = input("Ваш ответ: ")
        a = c.encrypt(message.encode())
        client_socket.send(a)
        g = client_socket.recv(1024)
        #h = c.decrypt(g).decode()
        print(f"Server: {g.decode()}")
start_client()
import socket
from cryptography.fernet import Fernet

key = Fernet.generate_key()

c = Fernet(key)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 9999))
    server_socket.listen(1)
    print("Сервер запуущен")
    con, addr = server_socket.accept()
    con.send(key)

    while True:
        d = con.recv(1024)
        #f = c.decrypt(d).decode()
        print(f"Клиент: {d.decode()}")
        r = input("Ответ: ")
        code = c.encrypt(r.encode())
        con.send(code)
    con.close()
start_server()
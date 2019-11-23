import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1025))
s.listen(5)
while True:
    client_socket, addr = s.accept()
    print(f"Connection to {addr} established")
    client_socket.send(bytes("This is the msg", "utf-8"))
    client_socket.close()

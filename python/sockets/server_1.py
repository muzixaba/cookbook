import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1025)) # port number must be four digits
s.listen(5) # queue of 5
while True:
    client_socket, address = s.accept()
    print(f"Connection to {address} established")
    client_socket.send(bytes("This is the msg", "utf-8"))
    client_socket.close()

import socket
import pickle

a = 10 #header size
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2133))
s.listen(5)
while True:
    client_socket, addr = s.accept()
    print(f"Connection to {addr} established")

    m = {"key1":"client", "key2":"server"}
    msg = pickle.dumps(m) #serialises the dict
    msg = bytes(f"{len(msg):<{a}}", "utf-8") + msg
    client_socket.send(msg)

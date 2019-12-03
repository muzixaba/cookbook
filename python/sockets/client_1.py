import socket
#AF_INET==ipv4 socket family, SOCK_STREAM==tcp (streaming socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1025)) # port=1025
# Use while loop keep receiving from the server until the entire message is done
message = ""
while True:
    msg = s.recv(10) # bytes/buffer=10 @least the header size
    if len(msg) <= 0:
        break
    message += msg.decode("utf-8")
print(message)
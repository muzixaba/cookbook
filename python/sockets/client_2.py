import socket
import pickle

a = 10 #header size
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),2133))

while True:
    complete_info = b'' # info comes in bytes
    rec_msg = True
    while True:
        mymsg = s.recv(16) # 16 bytes per transfer
        if rec_msg:
            print(f"Length of msg = {mymsg[:a]}")
            x = int(mymsg[:a])
            rec_msg = False
        complete_info += mymsg
        if len(complete_info)-a == x:
            print("Received complete info")
            print(complete_info[a:])
            # deserialise info
            m = pickle.loads(complete_info[a:])
            print(m)
            rec_msg = True
            complete_info = b''
    print(complete_info)
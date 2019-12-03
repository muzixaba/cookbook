import socket
import select # helps with cross platform os socket issues

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 1=True

server_socket.bind((IP, PORT))
server_socket.listen()
# list sockets for 'select' to keep track of
sockets_list = [server_socket]
# clients dict will keep track of {client_ip_addr: client username}
clients = {}

def receive_message(client_socket):
    """
    Receive messages from clients
    Message Type 1: Initial message
    Message Type 2: Chat message
    """
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header): # if client closes connection
            # didn't recv anything
            return False
        message_length = int(message_header.decode("utf-8").strip())
        return {
                "header":message_header,
                "data":client_socket.recv(message_length)
                }
    except:
        return False


while True:
    # interested in the first sockets_list
    # select.select(read_list, write_list, error_list)
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            user = receive_message(client_socket)
            if user is False:
                continue

            sockets_list.append(client_socket)
            clients[client_socket] = user

            print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username: {user['data'].decode('utf-8')}")
        
        else:
            message = receive_message(notified_socket)
            if message is False:
                print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            print(f"Receiver message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
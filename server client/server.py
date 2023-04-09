import socket

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_address = ('localhost', 8080)
sock.bind(server_address)

# listen for incoming connections (backlog of 1)
sock.listen(1)

while True:
    # wait for a connection
    print('waiting for a connection...')
    connection, client_address = sock.accept()
    print(f'connection from {client_address}')

    try:
        # receive the data in small chunks and send it back
        while True:
            data = connection.recv(16)
            if data:
                print(f'received "{data}"')
                connection.sendall(data)
            else:
                print(f'no more data from {client_address}')
                break

    finally:
        # close the connection
        connection.close()


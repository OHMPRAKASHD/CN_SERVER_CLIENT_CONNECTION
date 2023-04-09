import socket

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the server's address and port
server_address = ('localhost', 8080)
sock.connect(server_address)

try:
    # send some data
    message = 'This is a test message'
    print(f'sending "{message}"')
    sock.sendall(message.encode())

    # receive the response in small chunks
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(f'received "{data.decode()}"')

finally:
    # close the socket
    sock.close()


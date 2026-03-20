import socket

target_host = "127.0.0.1"
target_port = 65432

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

message = b"Hello, world!"
client.socket.sendall(message)

'''
response = client.recv(4096)

print(response.decode)
client.close()
'''
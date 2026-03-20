from http import client
import socket
import threading

IP = "127.0.0.1"
PORT = 65432

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # pass the IP address and port that you want the server to listen on
    server.bind(IP, PORT)

    # tell the server to start listening with a backlog queue of 5
    server.listen(5)
    print(f"Listening on {IP}: {PORT}")

    # server enters main loop where it waits for an incoming connection
    while True:

        # receive the client socket in the 'client' variable and the remote connection details in the 'address' variable
        server, address = server.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")

        # create a new thread object that points to the 'handle_client' function, and pass it the client socket object as an argument
        client_handler = threading.Thread(target=handle_client, args=(client,))

        # start the thread to handle the client connection
        client_handler.start()

# this is the point where the main server loop is ready to handle another incoming connection
# the 'handle_client' function performs the 'recv()' and then sends multiple simple messages back to the client
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1042)
        print(f"[*] Received: {request.decode("utf-8")}")

if __name__ == "__main__":        
    main()

# if you use the TCP client from earlier, you can send some test packets to the server
import socket

def start_client(host, port):
    # create a socket obj using the socket module 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # establish connection
    client_socket.connect((host, port))
    print("Connected to server.")

    while True:
        # allow the user to enter a message 
        message = input("Enter your message: ")
        # send the encoded message to the server through the client's socket 
        client_socket.send(message.encode())
        # create a way for the user to easily exit the program 
        if message.lower() == "bye":
            break
        # get the response from the server 
        response = client_socket.recv(1024)
        # print response from server 
        print("Server:", response.decode())

    # close the client socket 
    client_socket.close()

if __name__ == "__main__":
    HOST = "127.0.0.1" 
    PORT = 12345  
    start_client(HOST, PORT)

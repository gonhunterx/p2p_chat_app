import socket

def start_client(host, port):
    # create a socket obj using the socket module 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # establish connection
    client_socket.connect((host, port))
    print("Connected to server.")

    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode())
        if message.lower() == "bye":
            break
        response = client_socket.recv(1024)
        print("Server:", response.decode())

    client_socket.close()

if __name__ == "__main__":
    HOST = "127.0.0.1" 
    PORT = 12345  
    start_client(HOST, PORT)

import socket   

# start server function which will use the handle_client func to recieve the data from the client
# and print the message recieved from the client
def start_server(host, port):
    # socket settings 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server started. Waiting for connections...")
    
    # while loop for establishing the connection with the client 
    while True:
        client_socket, client_address = server_socket.accept()
        print("Connection established with", client_address)
        handle_client(client_socket)
        
def handle_client(client_socket):
    while True:
        # using try to catch any exceptions that might occur 
        try:
            # the recv method is called on the client socket obj. This waits for data to be recieved from the 
            # client 
            data = client_socket.recv(1024)
            if not data:
                break 
            print("Recieved message:", data.decode())
            # server waits for the user to input a message to send back 
            message = input("Enter message: ")
            # encode and send the message back 
            client_socket.send(message.encode())
        except ConnectionResetError:
            print("Client disconnected")
            break
        # close the client socket obj 
    client_socket.close() 
    
if __name__ == "__main__":
    HOST = "127.0.0.1"  # Change this to your IP if needed
    PORT = 12345  # Choose any free port
    start_server(HOST, PORT)
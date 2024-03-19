import socket

def client_program():
    host = socket.gethostname() 
    port = 50001  
 
    client_socket = socket.socket()  
 
    client_socket.connect((host, port)) 

    while True:
        message = input("Enter message to send to server: ")  
        client_socket.send(message.encode()) 
        if message.lower() == "exit":
            break

        response = client_socket.recv(1024).decode()  
        print('Received from server:', response)  

    client_socket.close() 
 
 
if __name__ == '__main__':
    client_program()

import socket
import threading

def handle_client(clientsocket, addr):
    clientsocket.settimeout(30)  # set timeout to 30 seconds
    while True:
        try:
            # Receive message from client
            msg = clientsocket.recv(1024).decode()
            if not msg:
                print(addr, 'disconnected')
                break
            print(f"Received from {addr[0]}:{addr[1]}: {msg}")

            # Send message back to client with server info
            responserom server at cket.send(server_info.encode())
        except socket.timeout:
            print("No message from client, moving on...")
        except Exception as e:
            print("Error:", e)
            break
    clientsocket.close()

s = socket.socket()
host = socket.gethostname()
port = 50001
print('server is listening on port', port)
s.bind((host, port))
s.listen(5)
try:
    while True:
        c, addr = s.accept()
        print("got connection from", addr)
        threading.Thread(target=handle_client, args=(c, addr)).start()
except KeyboardInterrupt:
    print("Server interrupted, closing...")
    s.close()

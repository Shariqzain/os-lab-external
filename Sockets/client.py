import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 5001))
print("Connected to server!")

client_socket.send("Hello from Client!".encode())

data = client_socket.recv(1024).decode()
print("Received from server:", data)

client_socket.close()

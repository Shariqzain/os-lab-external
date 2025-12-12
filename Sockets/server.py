import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5001))
server_socket.listen(1)

print("Server listening on port 5001...")

conn, addr = server_socket.accept()
print("Connected to:", addr)

data = conn.recv(1024).decode()
print("Received from client:", data)

conn.send("Hello from Server!".encode())

conn.close()
server_socket.close()

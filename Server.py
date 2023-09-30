import socket
import threading
import pickle
import json
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

# Define server settings
PORT = 5050
HOST = ""
SERVER_ADDR = (HOST, PORT)
FORMAT = "utf-8"

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address
server_socket.bind(SERVER_ADDR)

# Define a function to handle data reception
def receive_data(client_socket):
    try:
        received_data = b""  
        while True:
            chunk = client_socket.recv(1024)  # Read data in smaller chunks
            if not chunk:
                break  # No more data to read
            received_data += chunk  # Append the chunk to the received data
        return received_data
    except Exception as e:
        print(f"Error receiving data: {e}")
    return None

# Define a function to handle client connections
def handle_client(client_socket, client_addr):
    print(f"[NEW CONNECTION] {client_addr} is connected to the server")

    connected = True

    while connected:
        received_data = receive_data(client_socket)
        if not received_data:
            break  # Client disconnected

        # Process received_data as needed
        

    client_socket.close()

# Start the server
def start():
    server_socket.listen(5)
    print("[STARTING] server is starting...")

    while True:
        client_socket, client_addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_addr))
        thread.start()

if __name__ == "__main__":
    start()

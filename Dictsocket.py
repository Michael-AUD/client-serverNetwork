import socket
import pickle

# Create a dictionary
my_dict = {"name": "Jane Doe", "age": 30, "city": "Liverpool"}

# Convert the dictionary to bytes using pickle
data = pickle.dumps(my_dict)

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 5050)  # Change this to the server's address and port
client_socket.connect(server_address)

# Send the dictionary to the server
client_socket.send(data)

# Close the socket
client_socket.close()

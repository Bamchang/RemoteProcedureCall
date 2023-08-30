import socket
import json

def client_program():
    host = "127.0.0.1"
    port = 5001

    client_socket = socket.socket()
    client_socket.connect((host, port))

    request = {"method": "sqrt", "params": [4], "id": 1}
    client_socket.send(json.dumps(request).encode())

    data = client_socket.recv(1024).decode()
    response = json.loads(data)
    print(f"Received: {response}")

    client_socket.close()

if __name__ == "__main__":
    client_program()

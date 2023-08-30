import socket
import json

def sqrt(x):
    return x ** 0.5

def server_program():
    host = "127.0.0.1"
    port = 5001

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)
    print("Server is listening...")

    conn, address = server_socket.accept()
    print(f"Connection from {address}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        request = json.loads(data)
        method = request.get("method")
        params = request.get("params")
        id = request.get("id")

        if method == "sqrt":
            result = sqrt(*params)
            response = {"result": result, "id": id}
            conn.send(json.dumps(response).encode())

    conn.close()

if __name__ == "__main__":
    server_program()

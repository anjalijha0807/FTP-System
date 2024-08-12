import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)
        print("[CLIENT] Connected to server")

        with open("data/yt.txt", "r") as file:
            data = file.read()
            print("[CLIENT] File read successfully")

        client.send("yt.txt".encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        client.send(data.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

    except Exception as e:
        print(f"[ERROR]: {e}")
    finally:
        client.close()
        print("[CLIENT] Connection closed")

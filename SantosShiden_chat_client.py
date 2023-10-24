import socket
import threading

def handle_input(sock: socket.socket, stop_event: threading.Event):
    while not stop_event.is_set():
        msg = input()

        if msg == "!close":
            stop_event.set()

        sock.send(msg.encode())

def handle_recv(sock: socket.socket, stop_event: threading.Event):
    while not stop_event.is_set():
        data = sock.recv(1024).decode()

        if data == "Closing server.":
            stop_event.set()
            sock.send("!close".encode())
            data += "\nPress enter to exit."

        print(data)

def client(host: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((host, port))
            print("Connected to the server, close using !close.")

            stop_event = threading.Event()

            input_handler = threading.Thread(target=handle_input, args=(sock, stop_event))
            recv_handler = threading.Thread(target=handle_recv, args=(sock, stop_event))

            input_handler.start()
            recv_handler.start()

            input_handler.join()
            recv_handler.join()
        except ConnectionRefusedError:
            print("Connection refused, is the server online?")

    print("Exiting.")

client("127.0.0.1", 7)
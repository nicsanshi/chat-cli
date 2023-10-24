import socket
import threading

clients_sockets: list[socket.socket]

def handle_input(stop_event: threading.Event):
    while not stop_event.is_set():
        command = input()

        if command == "!close":
            stop_event.set()
        else:
            print(f"Command {command} unrecognised.")

def msg_to_all(msg: str):
    print(msg)
    for client_socket in clients_sockets:
        client_socket.send(msg.encode())

def handle_client(s: socket.socket, address: (str, int)):
    global clients_sockets
    global msg_to_all

    msg_to_all(f"{address} connected to the server.")

    with s:
        data = ""
        while data != "!close":
            data = s.recv(1024).decode()
            msg_to_all(f"{address}: {data}")

        clients_sockets.remove(s)

    msg_to_all(f"{address} disconnected from the server.")

def server(host: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        s.bind((host, port))
        s.listen()

        stop_event = threading.Event()
        input_handler = threading.Thread(target=handle_input, args=(stop_event,))
        input_handler.start()

        global clients_sockets
        clients_sockets = []

        print("Server online, close using !close")

        while not stop_event.is_set():
            try:
                client_socket, address = s.accept()

                clients_sockets.append(client_socket)

                client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
                client_handler.start()
            except TimeoutError:
                pass

        msg_to_all("Closing server.")

server("127.0.0.1", 7)

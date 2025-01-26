import socket
import sys

# Create a socket (connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print(f"Socket creation error: {msg}")

# Bind the socket and listen for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print(f"Binding the port {port}...")

        s.bind((host, port))  # Bind host and port using a tuple
        s.listen(5)  # Listen for connections
    except socket.error as msg:
        print(f"Socket binding error: {msg}\nRetrying...")
        bind_socket()

# Accept a connection from a client
def socket_accept():
    try:
        conn, address = s.accept()
        print(f"Connection established! IP: {address[0]}, Port: {address[1]}")
        send_command(conn)
        conn.close()
    except socket.error as msg:
        print(f"Error accepting connection: {msg}")

# Send commands to client
def send_command(conn):
    while True:
        cmd = input()  # Get command input from the server (you)
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()  # exit command module
        
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))  # Send command to the client
            
            client_response = str(conn.recv(1024), "utf-8")  # Receive response from client
            print("Output from client:\n", client_response)  # Print the response on the server side


def main():
    create_socket()
    bind_socket()
    socket_accept()

if __name__ == "__main__":
    main()

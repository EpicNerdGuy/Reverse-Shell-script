# Reverse-Shell-script

# Reverse Shell Script

A Python-based reverse shell script designed for educational and ethical hacking purposes. This project demonstrates the functionality of a reverse shell by providing both client and server components.

## Features
- Establishes a reverse connection from the client to the server.
- Enables remote command execution on the client system.
- Simple, modular code for easy understanding and modification.
- Designed for educational use in cybersecurity training.

## Components
- **Client Script**: The script that runs on the target machine and connects to the server.
- **Server Script**: The controlling script that listens for connections and sends commands.

## Usage
### Prerequisites
- Python 3.x installed on both the client and server machines.
- Ensure the firewall and network configurations allow the desired connection.

### Steps to Run
1. **Set Up the Server**:
   - Run the server script on your machine:  
     ```bash
     python3 server.py
     ```
   - The server will start listening for incoming connections.

2. **Set Up the Client**:
   - Run the client script on the target machine:  
     ```bash
     python3 client.py
     ```
   - Modify the server IP and port in the client script as needed.

3. **Interact**:
   - Once the connection is established, you can execute commands on the client system from the server.

### Example
- Start the server:  
  ```bash
  python3 server.py

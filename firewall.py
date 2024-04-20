import socket
import ipaddress

# Define allowed IP addresses and ports
ALLOWED_IPS = ["192.168.1.1", "10.0.0.1"]
ALLOWED_PORTS = [80, 443]

def is_allowed(address, port):
    """
    Check if the given address and port combination is allowed.
    """
    ip = ipaddress.ip_address(address)
    if str(ip) in ALLOWED_IPS and port in ALLOWED_PORTS:
        return True
    return False

def firewall():
    """
    Simple firewall implementation.
    """
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to localhost and port 8080
    s.bind(('localhost', 8080))
    
    # Listen for incoming connections
    s.listen(5)
    print("Firewall is running...")
    
    while True:
        # Accept a connection
        client_socket, address = s.accept()
        
        # Check if connection is allowed
        if is_allowed(address[0], address[1]):
            print(f"Connection from {address} allowed.")
            client_socket.send("Connection allowed.\n".encode())
            client_socket.close()
        else:
            print(f"Connection from {address} blocked.")
            client_socket.send("Connection blocked.\n".encode())
            client_socket.close()

if __name__ == "__main__":
    firewall()

#!/usr/bin/env python3

import socket
import sys

def check_port(target, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt

        # Try to connect to the target on the specified port
        result = sock.connect_ex((target, port))

        # If the connection is successful (returns 0), the port is open
        if result == 0:
            print(f"Port {port} is open on {target}")
        else:
            print(f"Port {port} is closed on {target}")

        # Close the socket
        sock.close()
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: scan <IP_or_domain> <port>")
        sys.exit(1)

    target = sys.argv[1]
    port = int(sys.argv[2])

    check_port(target, port)

if __name__ == '__main__':
    main()


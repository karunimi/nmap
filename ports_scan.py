#!/usr/bin/env python3

import socket
import sys

def check_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is open on {target}")
        else:
            print(f"Port {port} is closed on {target}")

        sock.close()
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: scan <IP_or_domain> <port1,port2,...>")
        sys.exit(1)

    target = sys.argv[1]
    ports = sys.argv[2].split(',')

    for port in ports:
        try:
            port = int(port)  # Convert each port string to an integer
            check_port(target, port)
        except ValueError:
            print(f"Invalid port number: {port}")

if __name__ == '__main__':
    main()

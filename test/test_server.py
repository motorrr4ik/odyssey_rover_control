import socket
import numpy as np
import time
import tty 
import sys 

HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 6677  # Port to listen on (non-privileged ports are > 1023)
tty.setcbreak(sys.stdin)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            control_key = (sys.stdin.read(1))
            conn.sendall(control_key.encode())
            #time.sleep(1.0)


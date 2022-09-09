import socket
import numpy as np
import random

#message = np.array([1,2], np.uint8)
#message = message.tobytes()
#
sock = socket.socket()
sock.connect(('localhost', 9999))

while True:
    sock.send(np.array([random.randint(0, 100), 0])), np.uint8
sock.close()


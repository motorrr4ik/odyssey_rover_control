import socket
import numpy as np
import time

EVAL_PC_HOST = '192.168.1.160'
EVAL_PC_PORT = 7777


class Client:
    def __init__(self):
        self.client_socket = None
        self.init_client_socket()

    def __del__(self):
        if self.client_socket:
            self.client_socket.close()

    def init_client_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((EVAL_PC_HOST, EVAL_PC_PORT))

    def close_connection(self):
        self.client_socket.close()

    def get_message(self):
        message = np.frombuffer(self.client_socket.recv(10000), np.float64)
        return message

if __name__ == "__main__":
    client = Client()
    while True:
        message = client.get_message()
        print(message)

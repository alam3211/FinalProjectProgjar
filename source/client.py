import socket
import os
import threading

TARGET_IP = "127.0.0.1"
TARGET_PORT = 8889
TARGET = (TARGET_IP, TARGET_PORT)

class Client:
    def __init__(self, target):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect(target)
    def run(self):
        outThread = threading.Thread(target=self.handleOutput)
        outThread.run()
        self.handleInput()
    def handleOutput(self):
        rawData = self.conn.recv(1024)
        print "In >> " + rawData
    def handleInput(self):
        while True:
            inData = raw_input()
            sock.send(inData)


client = Client(TARGET)
client.run()

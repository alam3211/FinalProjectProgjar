import socket
import os
import threading
import select

TARGET_IP = "127.0.0.1"
TARGET_PORT = 8889
TARGET = (TARGET_IP, TARGET_PORT)

class Client:
    def __init__(self, target):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect(target)
    def run(self):
        print "Running"
        self.handleInput()
    def handleOutput(self):
        rawData = self.recv()
        print "In >> " + rawData
    def handleInput(self):
        while True:
            print "Out << ",
            inData = raw_input()
            self.send(inData)
            self.handleOutput()
    def recv(self):
        return str(self.conn.recv(1024)).rstrip()
    def send(self, data):
        self.conn.send(str(data).ljust(1024))
    


client = Client(TARGET)
client.run()

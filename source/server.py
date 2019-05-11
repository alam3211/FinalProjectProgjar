import socket
import socket
import threading
import thread
import time
import sys
import json
import signal
from chat import Chat

chatserver = Chat()

class ProcessTheClient(threading.Thread):
	def __init__(self,connection,address):
		self.connection = connection
		self.address = address
		threading.Thread.__init__(self)

	def run(self):
		while True:
			data = self.connection.recv(1024)
			if data:
				self.connection.sendall(json.dumps(chatserver.proses(data)))
			else:
				break
		self.connection.close()

	def recv(self):
		return str(self.connection.recv(1024)).rstrip()
	def send(self, data):
		self.connection.send(str(data).ljust(1024))

class Server(threading.Thread):
	def __init__(self):
		self.the_clients = []
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		threading.Thread.__init__(self)

	def run(self):
		self.my_socket.bind(('0.0.0.0',8889))
		self.my_socket.listen(1)
		while True:
			self.connection, self.client_address = self.my_socket.accept()
			print >> sys.stderr, 'connection from', self.client_address
			
			clt = ProcessTheClient(self.connection, self.client_address)
			clt.start()
			self.the_clients.append(clt)
	

def main():
	def sigint_handler(signal, frame):
		sys.exit(0)
	signal.signal(signal.SIGINT, sigint_handler)
	svr = Server()
	svr.start()


if __name__=="__main__":
	main()


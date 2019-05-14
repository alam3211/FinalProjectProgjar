import socket
import socket
import threading
import thread
import time
import sys
import json
import signal
import chat
import smartconn

chatserver = chat.Chat()

class ProcessTheClient(threading.Thread):
	def __init__(self,connection,address):
		self.conn = smartconn.SmartConnection(connection)
		self.address = address
		threading.Thread.__init__(self)

	def run(self):
		while True:
			data = self.conn.recv()
			if data:
				res = json.dumps(chatserver.proses(data, self.conn))
				self.conn.send(res)
			else:
				break
		self.conn.close()

	

class Server(threading.Thread):
	def __init__(self):
		self.the_clients = []
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		threading.Thread.__init__(self)

	def run(self):
		self.my_socket.bind(('0.0.0.0',8889))
		self.my_socket.listen(100)
		print "Server started"
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


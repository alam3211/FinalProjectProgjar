from socket import *
import socket
import threading
import thread
import time
import sys
import json
from http import HttpServer

httpserver = HttpServer()

class ProcessTheClient(threading.Thread):
	def __init__(self,connection,address):
		self.connection = connection
		self.address = address
		threading.Thread.__init__(self)

	def run(self):
		while True:
			data = self.connection.recv(1024)
			if data:
				self.connection.sendall("{}" . format(httpserver.proses(data)))
                                break
			else:
				break
		self.connection.close()

class Server(threading.Thread):
	def __init__(self,portnumber):
		self.portnumber = portnumber
		self.the_clients = []
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		threading.Thread.__init__(self)

	def run(self):
		self.my_socket.bind(('0.0.0.0',self.portnumber))
		self.my_socket.listen(1)
		while True:
			self.connection, self.client_address = self.my_socket.accept()
			print >> sys.stderr, 'connection from', self.client_address
			
			clt = ProcessTheClient(self.connection, self.client_address)
			clt.start()
			self.the_clients.append(clt)
	

def main():
	portnumber=8887
	try:
	   portnumber=int(sys.argv[1])
	except:
	   pass
	svr = Server(portnumber)


if __name__=="__main__":
	main()


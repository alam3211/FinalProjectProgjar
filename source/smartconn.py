import socket

class SmartConnection:
    def __init__(self, conn):
        self.conn = conn

    def read_socket(self):
		return str(self.conn.recv(1024)).rstrip()
	
    def write_socket(self,data):
		self.conn.send(str(data).ljust(1024))

    def recv(self):
		rec = self.read_socket()
		res = rec
		while len(rec) == 1024:
			rec = self.read_socket()
			res += rec
		return res

    def send(self, data):
        while len(data) > 1024:
            sliced = data[:1024]
            self.write_socket(sliced)
            data = data[1024:]
        self.write_socket(data)

    def close(self):
        self.conn.close()
        
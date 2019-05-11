import sys
import os
import json
import uuid
from queue import Queue

class Chat:
	def __init__(self):
		self.sessions={}
		self.users = {}
	def proses(self,data):
		inData=data.split(" ")
		for i in range(len(inData)):
			inData[i] = inData[i].strip()
		try:
			command=inData[0]
			if (command=='auth'):
				username=inData[1]
				password=inData[2]
				return self.autentikasi_user(username,password)
			elif command == "send":
				sessId = inData[1]
				usernameFrom = self.sessions[sessId]['username']
				usernameDest = inData[2]
				message = inData[3]
				return self.send_message(sessId, username_from, username_dest, message)
			elif command == "inbox":
				sessId = inData[1]
				username = inData[2]
				return self.get_inbox(sessId, username)
			else:
				return {'status': 'ERROR', 'message': 'Protocol Tidak Benar'}
		except IndexError:
			return {'status': 'ERROR', 'message': 'Protocol Tidak Benar'}
	def create_user(self, username, password, name, nationality):
		if username in self.users:
			return {'status': 'ERROR', 'message': 'Username sudah digunakan'}
		self.users[username] = {'name' : name, 'nationality': nationality, 'password': password, 'incoming' : {}, 'outgoing': {}}
		return self.users[username]
	def autentikasi_user(self,username,password):
		if (username not in self.users):
			return { 'status': 'ERROR', 'message': 'User Tidak Ada' }
 		if (self.users[username]['password']!= password):
			return { 'status': 'ERROR', 'message': 'Password Salah' }
		tokenid = str(uuid.uuid4()) 
		self.sessions[tokenid]={ 'username': username, 'userdetail':self.users[username]}
		return { 'status': 'OK', 'tokenid': tokenid }
	def get_user(self,username):
		if (username not in self.users):
			return False
		return self.users[username]
	def send_message(self,sessionid,username_from,username_dest,message):
		if (sessionid not in self.sessions):
			return {'status': 'ERROR', 'message': 'Session Tidak Ditemukan'}
		s_fr = self.get_user(username_from)
		s_to = self.get_user(username_dest)
		
		if (s_fr==False or s_to==False):
			return {'status': 'ERROR', 'message': 'User Tidak Ditemukan'}

		message = { 'msg_from': s_fr['nama'], 'msg_to': s_to['nama'], 'msg': message }
		outqueue_sender = s_fr['outgoing']
		inqueue_receiver = s_to['incoming']
		try:	
			outqueue_sender[username_from].put(message)
		except KeyError:
			outqueue_sender[username_from]=Queue()
			outqueue_sender[username_from].put(message)
		try:
			inqueue_receiver[username_from].put(message)
		except KeyError:
			inqueue_receiver[username_from]=Queue()
			inqueue_receiver[username_from].put(message)
		return {'status': 'OK', 'message': 'Message Sent'}

	def get_inbox(self,sessId, username):
		if (sessionid not in self.sessions):
			return {'status': 'ERROR', 'message': 'Session Tidak Ditemukan'}
		s_fr = self.get_user(username)
		incoming = s_fr['incoming']
		msgs={}
		for users in incoming:
			msgs[users]=[]
			while not incoming[users].empty():
				msgs[users].append(s_fr['incoming'][users].get_nowait())
		return {'status': 'OK', 'messages': msgs}

















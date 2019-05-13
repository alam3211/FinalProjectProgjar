import sys
import os
import json
import uuid
import traceback
import urlparse
import hashlib
import base64
import shutil
import smartfile
import Queue

class Chat:
	def __init__(self):
		self.hashSalt = os.urandom(128)
		self.sessions = {}
		self.users = {}
		self.baseDir = "server/user"
		if os.path.isdir(self.baseDir):
			shutil.rmtree(self.baseDir)
		os.makedirs(self.baseDir)

	def proses(self,data):
		print "In >> " + data
		data = data.rstrip()
		splitted = data.split(" ")
		try:
			command = splitted[0]
			param = urlparse.parse_qs(splitted[1])
			for key in param.keys():
				param[key] = param[key][0]
			executer = None
			packed = ()
			print param
			if command == "auth":
				username = param['username']
				password = param['password']
				packed = (username, password)
				executer = self.autentikasi_user
			elif command == "file_list":
				sessionData = self.get_session(param['session'])
				username = self.get_user(sessionData['username'])
				packed = (username)
				executer = self.list_file
			elif command == "file_get":
				sessionData = self.get_session(param['session'])
				username = self.get_user(sessionData['username'])
				fileName = param['filename']
				packed = (username, fileName)
				executer = self.get_file
			elif command == "file_send":
				sessionData = self.get_session(param['session'])
				fromUsername = self.get_user(sessionData['username'])
				destUsername = self.get_user(param['username'])
				fileName = param['filename']
				payload = param['payload']
				packed = (fromUsername, destUsername, fileName, payload)
				executer = self.send_file
			elif command == "logout":
				sessionData = self.get_session(param['session'])
				sessId = param['session']
				packed = (sessId)
				executer = self.logout
			elif command == "send":
				sessionData = self.get_session(param['session'])
				usernameFrom = sessionData['username']
				usernameDest = param['destination']
				message = param['message']
				packed = (usernameFrom, usernameDest, message)
				executer = self.send_message
			elif command == "inbox":
				sessionData = self.get_session(param['session'])
				username = sessionData['username']
				packed = (username)
				executer = self.get_inbox
			elif command == "register":
				username = param['username']
				password = param['password']
				name = param['name']
				nationality = param['nationality']
				packed = (username, password, name, nationality)
				executer = self.register
			else:
				return {'status': 'ERROR', 'message': 'Fitur belum tersedia'}
			return executer(*packed)
		except Exception as e:
			return {'status': 'ERROR', 'message': 'Protocol Tidak Benar', 'error': str(e.message)}

	def send_file(self, fromUsername, destUsername, fileName, encodedFile):
		userFrom = self.get_user(fromUsername)
		userDest = self.get_user(destUsername)
		if fileName in userDest['files']:
			raise Exception("File dengan nama [" + fileName + "] sudah pernah ada")
		
		try:
			encodedFile = base64.b64decode(encodedFile)
			fileLoc = self.baseDir+"/"+destUsername+"/"+fileName
			smartFile = smartfile.SmartFile(fileLoc)
			smartFile.write(encodedFile)
		except Exception as e:
			raise Exception("Gagal mengirim file : " + e.message)
		userDest['files'][fileName] = userFrom['name']
		return {'status': "OK", 'message': 'File disimpan sebagai : ' + fileName}

	def list_file(self, username):
		user = self.get_user(username)
		keys = user['files'].keys()
		keys = json.dumps(keys)
		return {'status': "OK", 'file': keys}

	def get_file(self, username, fileName):
		user = self.get_user(username)
		if fileName not in user['files']:
			raise Exception("File dengan nama [" + fileName + "] tidak ditemukan")
		try:
			fileLoc = self.baseDir+"/"+username+"/"+fileName
			smartFile = smartfile.SmartFile(fileLoc)
			smartFile.read()
			rawFile = smartFile.get_representation()
			encodedFile = base64.b64encode(rawFile)
		except Exception as e:
			raise Exception("Gagal mengirimkan file : " + e.message)
		return {'status': "OK", 'name':fileName, 'payload': encodedFile}

	def get_session(self, sessId):
		if sessId not in self.sessions:
			raise Exception("Session dengan id [" + sessId + "] tidak dapat ditemukan")
		return self.sessions[sessId]

	def register(self, username, password, name, nationality):
		if username in self.users:
			raise Exception("Username [" + username + "] sudah digunakan!")
		self.users[username] = {'name' : name, 'nationality': nationality, 'password': self.get_hashed(password), 'incoming' : {}, 'outgoing': {}, 'files': {}}
		return {'status': "OK", 'username': username, 'name': name, 'nationality': nationality}

	def autentikasi_user(self,username,password):
		user = self.get_user(username)
 		if (user['password'] != self.get_hashed(password)):
			raise Exception("Password tidak benar")
		tokenid = str(uuid.uuid4()) 
		self.sessions[tokenid]={ 'username': username, 'userdetail':self.users[username]}
		return { 'status': 'OK', 'tokenid': tokenid }
	
	def logout(self, sessId):
		if sessId not in self.sessions:
			raise Exception("Session tidak ditemukan")
		self.sessions.pop(sessId)
		return {'status': 'OK', 'message': 'Berhasil keluar'}
	
	def get_user(self,username):
		if (username not in self.users):
			raise Exception("Username dengan nama [" + username + "] tidak dapat ditemukan")
		return self.users[username]

	def get_hashed(self, plainText):
		return hashlib.sha512(plainText + self.hashSalt).hexdigest()

	def send_message(self,username_from,username_dest,message):
		s_fr = self.get_user(username_from)
		s_to = self.get_user(username_dest)

		message = { 'msg_from': s_fr['name'], 'msg_to': s_to['name'], 'msg': message }
		outqueue_sender = s_fr['outgoing']
		inqueue_receiver = s_to['incoming']
		try:	
			outqueue_sender[username_from].put(message)
		except KeyError:
			outqueue_sender[username_from]=Queue.Queue()
			outqueue_sender[username_from].put(message)
		try:
			inqueue_receiver[username_from].put(message)
		except KeyError:
			inqueue_receiver[username_from]=Queue.Queue()
			inqueue_receiver[username_from].put(message)
		return {'status': 'OK', 'message': 'Message Sent'}

	def get_inbox(self, username):
		s_fr = self.get_user(username)
		incoming = s_fr['incoming']
		msgs={}
		for users in incoming:
			msgs[users]=[]
			while not incoming[users].empty():
				msgs[users].append(s_fr['incoming'][users].get_nowait())
		return {'status': 'OK', 'messages': msgs}

















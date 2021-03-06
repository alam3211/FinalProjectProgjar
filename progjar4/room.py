import select
import json
import traceback
import os
import base64
import smartfile
import shutil

class Room:
    def __init__(self, name):
        self.roomname = name
        self.names = []
        self.clients = {}
        self.files = {}
        self.roomDir = "server/room"
        if os.path.isdir(self.roomDir):
            shutil.rmtree(self.roomDir)
        os.makedirs(self.roomDir)

    def broadcast(self, sender, message):
        errorClient = []
        display = sender
        if sender != "[System]":
            display = self.clients[sender]['display']
        packed = {'status': "OK", 'type':"broadcast", 'display': display, 'messages': message, 'username': sender}
        for key in self.clients:
            client = self.clients[key]
            try :
                client['conn'].send(json.dumps(packed))
            except Exception as e:
                traceback.print_exc()
                errorClient.append(key)
            
        for client in errorClient:
            self.clients.pop(client['username'])
    
    def send_file(self, fromUsername, roomName, fileName, encodedFile):
		try:
			os.mkdir(self.roomDir+"/"+roomName)
			encodedFile = base64.b64decode(encodedFile)
			fileLoc = self.roomDir+"/"+roomName+"/"+fileName
			smartFile = smartfile.SmartFile(fileLoc)
			smartFile.write(encodedFile)
		except Exception as e:
			raise Exception("Gagal mengirim file : " + e.message)
		return {'status': "OK", 'message': fileName}

    def get_client_count(self):
        return len(self.clients)

    def get_clients_name(self):
        return self.names

    def update_clients_name(self):
        self.names = []
        for key in self.clients:
            self.names.append(self.clients[key]['display']) 
    
    def add_client(self, username, displayName, conn):
        if username in self.clients:
            self.remove_client(username)
        self.broadcast("[System]", "User ["+displayName+"] telah bergabung dengan chat!")
        self.clients[username] = {'username': username, 'conn': conn, 'display': displayName}
        self.update_clients_name()

    def remove_client(self, username):
        if username not in self.clients:
            raise Exception("Username tidak ditemukan!")
        displayName = self.clients[username]['display']
        self.clients.pop(username)
        self.broadcast("[System]", "User ["+displayName+"] telah meniggalkan chat!")
        self.update_clients_name()
    

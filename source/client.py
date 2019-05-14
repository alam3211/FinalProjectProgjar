import socket
import os
import threading
import select
import smartconn
import urllib
import getpass
import json
import shutil
import smartfile
import base64
import sys
import traceback

TARGET_IP = "127.0.0.1"
TARGET_PORT = 8889
TARGET = (TARGET_IP, TARGET_PORT)

class Client:
    def __init__(self, target):
        self.isSynchronous = True
        self.sessionId = None
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect(target)
        self.conn = smartconn.SmartConnection(self.conn)
        self.baseDir = "client/user"
    def run(self):
        print "Running"
        while True:
            if self.isSynchronous:
                self.handle_synchronous()
            else:
                self.handle_asynchronous()

    def handle_asynchronous(self):
        rawSock = self.conn.raw_socket()
        print "Out: ",
        sys.stdout.flush()
        try:
            readAbleSockets, writeAbleSockets, errorSockets = select.select([sys.stdin, rawSock], [], [])
            for reader in readAbleSockets:
                if reader == self.conn.raw_socket():
                    print '\r',
                    response = self.get_response()
                    self.handle_async_response(response)
                else :
                    message = sys.stdin.readline()
                    self.send_request("room_chat", {"message": message, "session": self.sessionId})
        except KeyboardInterrupt as e:
            self.send_request('room_leave', {'session': self.sessionId})
            response = self.get_response()
            if response['status'] == "OK":
                self.isSynchronous = True
                print response['messages']
            else:
                print response['error']
            

    def handle_async_response(self, response):
        if "type" in response:
            if response['type'] == "broadcast" and response['username'] != self.username:
                print "In["+response['display'] + "]: " + response['messages'].rstrip()
            

    def handle_synchronous(self):
        try:
            if self.sessionId == None:
                command = raw_input("Command [login|register] : ")
                command = command.lower()
                if command == "login":
                    self.perform_login()
                elif command == "register":
                    self.perform_register()
            else:
                command = raw_input("Command [chat|send file|get file|list file|inbox|join room|logout] : ")
                command = command.lower()
                if command == "chat":
                    self.process_chat()
                elif command == "send file":
                    self.process_send_file()
                elif command == "get file":
                    self.process_get_file()
                elif command == "list file":
                    self.process_list_file()
                elif command == "inbox":
                    self.perform_inbox()
                elif command == "join room":
                    self.perform_room_join()
                elif command == "logout":
                    self.perform_logout()

        except Exception as e:
            print "Error! " + e.message

    def process_chat(self):
        destUsername = raw_input("Recipient username: ")
        message = raw_input("Message: ")
        request = {"session": self.sessionId, "destination": destUsername, "message": message}
        self.send_request("send", request)
        response = self.get_response()
        if response['status'] == "OK":
            print response['message']+" to user ["+ response['user']+"]."
        else:
            raise Exception(response['error'])

    def process_list_file(self):
        self.send_request("file_list", {'session': self.sessionId})
        response = self.get_response()
        if response['status'] == "OK":
            print response['file']
        else:
            raise Exception(response['error'])

    def process_send_file(self):
        fileName = raw_input("File Name: ")
        destUsername = raw_input("Recipient Username: ")
        rawFile = smartfile.SmartFile(self.baseDir+"/"+self.username+"/"+fileName)
        rawFile.read()
        payload = rawFile.get_representation()
        payload = base64.b64encode(payload)
        self.send_request("file_send", {'session': self.sessionId, 'filename': fileName, 'payload': payload, 'username': destUsername})
        response = self.get_response()
        if response['status'] == "OK":
            print "Berhasil mengirim file ! "+ response['message']+" telah dikirim."
        else:
            raise Exception(response['error'])
        

    def process_get_file(self):
        fileName = raw_input("Remote File Name: ")
        self.send_request("file_get", {'session': self.sessionId, 'filename': fileName})
        response = self.get_response()
        if response['status'] == "OK":
            payload = response['payload']
            payload = base64.b64decode(payload)
            targetFile = smartfile.SmartFile(self.baseDir+"/"+self.username+"/"+fileName)
            targetFile.write(payload)
            print response['name']
        else:
            raise Exception(response['error'])

    
    def perform_logout(self):
        self.send_request("logout", {'session': self.sessionId})
        response = self.get_response()
        if response['status'] == "OK":
            self.sessionId = None
            print "Bye Bye!"
        else:
            raise Exception(response['error'])

    def perform_inbox(self):
        self.send_request("inbox", {'session': self.sessionId})
        response = self.get_response()
        if response['status'] == "OK":
            print str(len(response['messages']))+" messages incoming."
            for key in response['messages'].keys():
                for message in response['messages'][key]:
                    print "from "+message['msg_from']+": "+message['msg']
        else:
            raise Exception(response['error'])

    def perform_room_join(self):
        roomname = raw_input("Room Code: ")
        self.send_request("room_join", {'session': self.sessionId, 'roomname': roomname})
        response = self.get_response()
        if response['status'] == "OK":
            self.isSynchronous = False
            print response['messages']
            print "List User : "
            for index in range(len(response['users'])):
                print str(index+1) + '. ' +response['users'][index]
        else:
            raise Exception(response['error'])
        

    def perform_register(self):
        username = raw_input("Username: ")
        password = getpass.getpass()
        name = raw_input("Name: ")
        nationality = raw_input("Nationality: ")
        payload = {"username": username, "password": password, "nationality": nationality, "name": name}
        self.send_request("register", payload)
        response = self.get_response()
        if response['status'] == "OK":
            print "User berhasil dibuat"
        else:
            raise Exception(response['error'])

    def perform_login(self):
        print "Username : ",
        username = raw_input()
        password = getpass.getpass()
        payload = {"username": username, "password": password}
        self.send_request("auth", payload)
        response = self.get_response()
        if response['status'] == "OK":
            self.sessionId = response['tokenid']
            self.username = username
            self.prepare_directory(username)
            print "Login ["+username+"] telah berhasil"
        else:
            raise Exception("Gagal melakukan login, " + response['error'])

    def prepare_directory(self, name):
        clientDir = self.baseDir + "/"+name
        if not os.path.exists(clientDir):
            os.makedirs(clientDir)

    def send_request(self, command, payload):
        encoded = urllib.urlencode(payload)
        self.conn.send(command + " " + encoded)

    def get_response(self):
        return json.loads(self.conn.recv())

if __name__ == "__main__":
    client = Client(TARGET)
    client.run()

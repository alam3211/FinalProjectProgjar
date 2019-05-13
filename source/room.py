class Room:
    def __init__(self):
        self.clients = {}
        self.files = {}
    
    def get_client_count(self):
        return len(self.clients)
    
    def add_client(self, username, conn):
        if username in self.clients:
            raise Exception("Username sudah berada di dalam")
        self.clients['username'] = conn

    def remove_client(self, username):
        self.clients.pop(username)
    

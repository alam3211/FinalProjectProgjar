import base64

class SmartFile:
    def __init__(self, filePath):
        self.fileLoc = filePath
        
    def read(self):
        fp = open(self.fileLoc, "r")
        self.rawFile = fp.read()
        fp.close()

    def write(self, payload):
        self.rawFile = payload
        fp = open(self.fileLoc, "wb+")
        fp.write(payload)
        fp.close()


    def get_representation(self):
        return self.rawFile
import sys
sys.dont_write_bytecode = True
import socket
from config import Config
import hashlib


class Node:
    def __init__(self, nodeID, nodeIP, nodePort):
        self.nodeID = nodeID
        self.ip = nodeIP
        self.port = nodePort
        self.address = (self.ip, self.port)
        self.connected = False
    
    def connect(self, clientSocket:socket.socket):
        try:
            clientSocket.connect((self.ip, self.port))
            print(f"Connected to '{self.nodeID}")
            self.connected = True
            return True
        except:
            print(f"Failed to connect to '{self.nodeID}")
            self.connected = False
            return False
    
    def disconnect(self, clientSocket:socket.socket):
        try:
            clientSocket.close()
            print(f"Disconnected from '{self.nodeID}")
            self.connected = True
            return True
        except:
            print(f"Failed to disconnect from '{self.nodeID}")
            self.connected = False
            return False
    
    def respond(self, clientSocket:socket.socket, message:str):
        try:
            clientSocket.sendto(str.encode(message), self.address)
            return True
        except:
            return False
    
        

        
    class Query:  

        '''
        Query Types
        -----------
        0 - ping: no response
        1 - request file: return file

        '''

        def connected(clientSocket:socket.socket):
            try:
                queryType = 0
                print("init")
                queryMsg = f"{str(queryType):<{Config.headerFormat.typeLen}}"
                clientSocket.sendto(str.encode(queryMsg), Node.address)
                return True 
            except:
                return False

        def requestFile(clientSocket:socket.socket, filePath:str):
            queryType = 1
            queryMsg = f"{f'{queryType}' :< {Config.headerFormat.typeLen}}" + hashlib.sha256(str.encode(filePath)).hexdigest()
            try:
                clientSocket.sendto(str.encode(queryMsg), Node.address)
                print(f"Requested '{filePath}' from {Node.nodeID}({Node.ip}:{Node.port})")
                return True
            except:
                print(f"Failed to request '{filePath}' from {Node.nodeID}({Node.ip}:{Node.port})")
                return False

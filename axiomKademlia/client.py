import sys
sys.dont_write_bytecode = True
import socket
from config import Config
from node import Node
import hashlib

class Client:
	def __init__(self, nodeID)
		self.nodeID = nodeID
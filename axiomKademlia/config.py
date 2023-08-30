import yaml
import sys
sys.dont_write_bytecode = True

with open("axiomKademlia/config.yml", "r") as config:
        data = yaml.safe_load(config)

class Config:
    class bootstrap:
        nodeID = data["bootstrap"]["nodeID"]
        IP = data["bootstrap"]["IP"]
        port = data["bootstrap"]["port"]

    class headerFormat:
        typeLen = data["headerFormat"]["typeLen"]
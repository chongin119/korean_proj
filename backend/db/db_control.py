import sqlite3
from db_config import Config

class DB:
    def __init__(self,path):
        self.db = sqlite3.connect(path)


    def __del__(self):
        self.db.close()

    def insert(self):
        pass

if __name__ == "__main__":
    db = DB("korean.db")

    test = []

    for i,pth in enumerate(Config["path"].values()):
        with open(pth,'r',encoding="utf-16") as f:
            test = f.read()
            print(test)
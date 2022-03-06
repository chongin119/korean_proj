import sqlite3
from db_config import Config

class DB:
    def __init__(self,path):
        self.db = sqlite3.connect(path)


    def __del__(self):
        pass

if __name__ == "__main__":
    db = DB("korean.db")
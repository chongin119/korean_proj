import sqlite3
from db_config import Config

class DB:
    def __init__(self,path):
        self.db = sqlite3.connect(path)


    def __del__(self):
        self.db.close()

    def insert(self,book):
        cursor = self.db.cursor()
        book_name = book[0][3:]
        book_level = 1
        publisher = book[1][4:]
        year = book[2][5:]
        author = book[3][3:]
        book_id = cursor.execute("select id from book order by id Desc ").fetchone()

        if book_id is None:
            book_id = 1
        else:
            book_id = book_id[0]+1

        cursor.execute("insert into book (id,book_name,book_level,author,publisher,year) values (?,?,?,?,?,?)",(book_id, book_name, book_level, author, publisher, year))

        #清除书名，出版社，年份，作者
        for cnt in range(4):
            del book[0]

        for line in book:
            chapter_id = ""
            if line.find("第") != -1:
                chapter_id = cursor.execute("select id from chapter order by id Desc").fetchone()

                if chapter_id is None:
                    chapter_id = 1
                else:
                    chapter_id = chapter_id[0]+1

                cursor.execute("insert into chapter (id,chapter_name,book_id) values (?,?,?)",(chapter_id,line,book_id))
            else:
                sent_id = cursor.execute("select id from sentences order by id Desc").fetchone()
                if sent_id is None:
                    sent_id = 1
                else:
                    sent_id = sent_id[0]+1

                cursor.execute("insert into sentences (id,content,length,next_sent_id,previous_sent_id,chapter_id) values (?,?,?,?,?,?)",(sent_id,line,len(line),sent_id+1,sent_id-1,chapter_id))


        self.db.commit()


if __name__ == "__main__":
    db = DB("korean.db")

    for i,pth in enumerate(Config["path"].values()):
        book = []
        with open(pth,'r',encoding="utf-16") as f:
            book = f.read().splitlines()
            db.insert(book)

    del db

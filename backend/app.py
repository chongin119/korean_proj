from flask import Flask,render_template,jsonify
from backend.db_control import DB

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/matching',methods=['GET','POST'])
def matching():
    pass

@app.route('/resulting',methods=['GET','POST'])
def resulting():
    db = DB(db_name)
    cont = db.show_all()
    cont_dic = {}
    for i in cont:
        cont_dic[i[0]] = i[1]
    del db

    return jsonify(cont_dic)

if __name__ == '__main__':
    db_name = "./db/korean.db"
    app.run(debug=True,port=3000)
from flask import Flask,render_template,jsonify
from flask_cors import CORS
from backend.db_control import DB

app = Flask(__name__)
CORS(app,resources={r'/*' : {'origin' : '*'}})

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
    req_list = []
    for i in cont:
        cont_dic = {}
        cont_dic['id'] = i[0]
        cont_dic['cont'] = i[1]
        req_list.append(cont_dic)
    del db

    return jsonify(req_list)

if __name__ == '__main__':
    db_name = "./db/korean.db"
    app.run(debug=True,port=3000)
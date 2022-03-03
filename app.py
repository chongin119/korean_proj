from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True,port=3000)
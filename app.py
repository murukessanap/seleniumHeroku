from flask import Flask
import getUrbanProData as gd

app = Flask(__name__)

@app.route("/")
def hello():
    #return "Hello World!"
    return gd.get()


if __name__ == '__main__':
    app.run(debug=True, host="192.168.1.103",port=5000)
    #app.run("--host=127.0.0.1 --port=1234")
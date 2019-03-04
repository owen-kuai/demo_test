from flask import Flask


app = Flask(__name__)


@app.route("/")
def hellow_world():
    a = 2
    b = 3443
    return a+b


if __name__ == '__main__':
    app.run(port=5000)
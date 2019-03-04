from flask import Flask


app = Flask(__name__)


@app.route("/")
def hellow_world():
    a = 2
    b = 3443
    c = 3434
    return a+b+c


if __name__ == '__main__':
    app.run(port=5000)

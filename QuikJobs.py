from flask import Flask
from flask import render_template
from flask import request
from flask import send_file

app = Flask(__name__)


@app.route('/', methods = ['GET','POST'])
def hello_world():
    return render_template("bootstrap-example.html")


if __name__ == '__main__':
    app.run(debug=True)

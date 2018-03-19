from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from forms import addJobs
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ihatelife'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///jobs.db"
db = SQLAlchemy(app)


@app.route('/addjobs', methods = ['GET','POST'])
def addjobs():
    form = addJobs();
    return render_template("addjobs.html", form=form)

@app.route('/', methods = ['GET','POST'])
def index():
    return render_template("bootstrap-example.html")


                                                        

if __name__ == '__main__':
    app.run()



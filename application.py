from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://sdqhgbpsslsjln:3e4c77038676a7796cb0d9dcf579e21105f5f690dba065fe22f01d507c256e58@ec2-54-243-193-59.compute-1.amazonaws.com:5432/d40523h3svja4i'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)


class admins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
#db.create_all()
#print ("working")
#x = admins(username = "maheen", password="testing")
#db.session.add(x)
#db.session.commit()
#print("worked")

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/about")
def aboutme():
	return render_template("about.html")

@app.route("/sections")
def sections():
    return render_template("work.html")

@app.route("/adminlogin")
def admin():
    return render_template("single.html")

@app.route("/loginfailed")
def logfai():
    return render_template("loginfailed.html")
@app.route("/logincheck",methods=['POST'])
def logincheck():
    username1 = request.form["username"]
    password1 = request.form["password"]
    print (username1)
    print(password1)
    DB_user = admins.query.filter_by(username=username1).first()
    DB_user2 = admins.query.filter_by(password=password1).first()
    if not(DB_user is None)  and not(DB_user2 is  None):

        if(DB_user.username==username1 and DB_user2.password== password1):
            return render_template("loggedin.html")
    return "WORKING"



app.debug = True
app.run()

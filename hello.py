from flask import Flask,url_for,request,render_template
import os

app = Flask(__name__)

@app.route('/logins',methods=['GET','POST'])

def login():
	if request.method == 'POST':
		return "User %s logged in " % request.form['username']
	return render_template("login.html")

if __name__ == '__main__':
	app.debug = True
	app.run()
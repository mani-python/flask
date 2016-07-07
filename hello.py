from flask import Flask,url_for,request,render_template
import os

app = Flask(__name__)

@app.route('/logins',methods=['GET','POST'])

def login():
	error = "None"
	if request.method == 'POST':
		if valid_login(request.form.get('username'),request.form.get('password')):
			return "Welcome back %s " % request.form['username']
		else:
			error = "Incorrect username and pwd"
			return render_template('login.html',error = error)
	return render_template("login.html")

def valid_login(username,password):
	if  username == password:
		return True
	else:
		return False

if __name__ == '__main__':
	app.debug = True
	app.run()
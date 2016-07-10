from flask import Flask,url_for,request,render_template,redirect,flash
import os

app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])

def login():
	error = "None"
	if request.method == 'POST':
		if valid_login(request.form.get('username'),request.form.get('password')):
			flash("Successfully logged in")
			return redirect(url_for('welcome',username=request.form.get('username')))			
		else:
			error = "Incorrect username and pwd"
			return render_template('login.html',error = error)
	return render_template("login.html")

def valid_login(username,password):
	if  username == password:
		return True
	else:
		return False

@app.route('/welcome/<username>')
def welcome(username):
	return render_template('welcome.html', username = username)

if __name__ == '__main__':
	app.secret_key='Super'
	app.debug = True
	app.run()
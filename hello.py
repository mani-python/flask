from flask import Flask,url_for,request
import os

app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])

def index():
	if request.method == 'POST':
		return 'username is ' + request.values["username"]
	else:
		return '<form method="post" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'

if __name__ == '__main__':
	app.debug = True
	app.run()
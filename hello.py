from flask import Flask,url_for
import os

app = Flask(__name__)

@app.route('/')

def index():
	return url_for('printuser', username='Mani')

@app.route('/user/<username>')

def printuser(username):
	return "Hello" + " " + username

@app.route('/post/<int:postid>')

def printpost(postid):
	return "Hello %d" % postid

if __name__ == '__main__':
	app.debug = True
	app.run()
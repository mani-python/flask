from flask import Flask,jsonify
import os
import json

app = Flask(__name__)

@app.route('/')

def  dirs():
	path = '/Users/mgovindarajan/Documents/Python/flask_init'
	dirs= os.listdir( path )
	return jsonify(dirs)
	

if __name__ == '__main__':
	app.debug = True
	app.run()

# path = '/Users/mgovindarajan/Documents/Python/flask_init'
# dirs= os.listdir( path )
# print(dirs)
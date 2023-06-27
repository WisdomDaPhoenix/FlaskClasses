from flask import Flask, render_template
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)


#BASE HTML PAGE
#--------------------

@app.route('/')

def home():
	return render_template("base.html", num=45), 200


if __name__=="__main__":
	app.run(port=4400, debug=True)



"""
Desc: backend for the online store
author: Oscar Rodriguez 

"""

from flask import Flask 
from test1 import about_me
app = Flask(__name__)
 
@app.route("/")
def home():
     return "hi there!"


@app.route("/")
def about():
    return f"{about_me['name']}{about_me['last']}"

#TODO remove debug before deploying
app.run(debug=True)

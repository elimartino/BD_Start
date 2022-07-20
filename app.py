import requests
import configparser
import os
from flask import Flask, render_template, request   
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("main.j2")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3005)) 

    app.run(host= '0.0.0.0', port=port)
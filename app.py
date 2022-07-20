import requests
import configparser
import os
from flask import Flask, render_template, request, redirect  

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("main.j2")


@app.route("/classes")
def classes():
    if request.method == 'GET':
        return render_template("classes.j2")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'GET':
        return render_template("contact.j2")
    if request.method== 'POST':
        subject= request.form["subject"]
        message= request.form["message"]
        email= request.form["email"]
        print(subject, message, email)
        return redirect("/")
        

    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3005)) 

    app.run(host= '0.0.0.0', port=port)
import requests
import configparser
import os
from flask import Flask, render_template, request, redirect , flash
import smtplib, ssl

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def root():
    return render_template("main.j2")



@app.route("/about")
def about():
    if request.method == 'GET':
        return render_template("about.j2")



@app.route("/classes")
def classes():
    if request.method == 'GET':
        return render_template("classes.j2")




@app.route("/gallery")
def gallery():
    if request.method == 'GET':
        return render_template("gallery.j2")




@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'GET':
        return render_template("contact.j2")
    if request.method== 'POST':
        email= request.form["email"]
        email_from="bdbasimops@gmail.com"
        p_word="pwutqljiigutsqwz"
        email_to="elimmartino@gmail.com"
        email_content= request.form["name"]+ request.form["message"]
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email_from, p_word)
            server.sendmail(email_from, email_to, email_content)
        flash('Message Submitted')
        return redirect("/")
        

    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3005)) 

    app.run(host= '0.0.0.0', port=port)
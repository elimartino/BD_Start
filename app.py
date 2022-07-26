import requests
import configparser
import os
from flask import Flask, render_template, request, redirect 
import smtplib, ssl

app = Flask(__name__)

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
        email_from="bdbasimops@gmail.com"
        p_word="pwutqljiigutsqwz"
        email_to="elimmartino@gmail.com"
        email_content="This is a test email"
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            # Provide Gmail's login information
            server.login(email_from, p_word)
            # Send mail with from_addr, to_addrs, msg, which were set up as variables above
            server.sendmail(email_from, email_to, email_content)
        subject= request.form["subject"]
        message= request.form["message"]
        email= request.form["email"]
        print('email sent')
        print(subject, message, email)
        return redirect("/")
        

    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3005)) 

    app.run(host= '0.0.0.0', port=port)
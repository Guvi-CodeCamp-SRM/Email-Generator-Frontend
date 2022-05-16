from math import prod
from flask import Flask, render_template, request, redirect

app=Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/welcome-email-template")
def welcome():
    return render_template("welcome-email.html")

@app.route("/meeting-invitation-template")
def meeting():
    return render_template("meeting-invitation.html")

@app.route("/product-launch-template")
def product():
    return render_template("product-launch.html")

@app.route("/podcast-invite-template")
def podcast():
    return render_template("podcast-invitation.html")

@app.route("/client-onboarding-template")
def client():
    return render_template("client-onboarding.html")

@app.route("/event-invitation-template")
def event():
    return render_template("event-invitation.html")

if __name__=="__main__":
    app.run(debug=False)
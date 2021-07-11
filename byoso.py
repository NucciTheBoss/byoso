#!/usr/bin/env python3
import RPi.GPIO as gp
from flask import Flask, render_template


# Initialize Flask application
app = Flask(__name__)

# Initialize RPi.GPIO
gp.setmode(gp.BCM)
gp.setwarnings(False)

# Initialize pin 17
pin = 17
gp.setup(pin, gp.OUT)
gp.output(pin, gp.HIGH)


# For when the byoso is first accessed via the web browser
@app.route("/")
def home():
    return render_template("on.html")


@app.route("/on")
def turn_on():
    gp.output(pin, gp.LOW)
    return render_template("off.html")


@app.route("/off")
def turn_off():
    gp.output(pin, gp.HIGH)
    return render_template("on.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

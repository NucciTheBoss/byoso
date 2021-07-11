#!/usr/bin/env python3
import RPi.GPIO as gp
from flask import Flask, render_template


# Initialize Flask application
app = Flask(__name__)

# Initialize RPi.GPIO
gp.setmode(gp.BCM)
gp.setwarnings(False)
outlet_off = [True]

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
    if outlet_off[0] is True:
        outlet_off[0] = False
        gp.output(pin, gp.LOW)
        return render_template("off.html")

    else:
        return render_template("on.html")


@app.route("/off")
def turn_off():
    if outlet_off is False:
        outlet_off[0] = True
        gp.output(pin, gp.HIGH)
        return render_template("on.html")

    else:
        return render_template("off.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

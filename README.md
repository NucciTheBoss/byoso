<p align="center">
    <img src="./share/logos/byoso.png" width="400">
</p>

<h3 align="center"><b>BYOSO</b></h3>

<p align="center">
    (B) Build (Y) Your (O) Own (S) Smart (O) Outlet using a Raspberry Pi Zero W, an outlet box, the Python Flask framework, and a simple internet connection!
    <br />
    <i>Pronounced "by"-"oh"-"so"</i>
</p>

<br />

## Introduction

Do you enjoy the convenience of having smart-IoT devices automate your day-to-day tasks like turning on the lights, adjusting the thermostat, or even brewing coffee for you in morning, but you despise the fact that said devices always need to be connected to a cloud server outside of your home to work? 

While cloud servers make it easier for embedded devices to perform large calculations or pull data vital to its operation, cloud servers introduce a multitude of security issues. What if someone hacks the cloud server and steals your personal data? Who is accessing the data collected by your device? What are they doing with said data? I'm sure that you could find vague answers to your questions, but you would probably have to spend at least two days hunting through the license agreement you have to sign before you can start using your smart device.

Don't like having to need a law degree to figure out where your personal data is going? Well, you are in luck. In this tutorial, I am going to teach you how to build your own smart outlet that does not require some half-a-million dollar server in the middle of the Arizona desert to work. This smart outlet, as I conveniently named BYOSO, does not require a cloud server to work! All it needs is some programming know how, elbow greese, and a working internet connection. Let's get into it then! 

## Table of Contents

* [How to make your own BYOSO](#how-to-make-your-own-byoso)
* [Copyright and License](#copyright-and-license)
* [Troubleshooting](#troubleshooting)

## How to make your own BYOSO

### Step 1: Get the parts

In order to successfully build a functioning BYOSO that does not electricute you, you will need to have the following parts on hand:

* 1 2-gang outlet box cover.
* 1 1-gang 1-switch outlet box cover.
* 2 2-gang 2-inch deep outlet box with 3/4-inch and 1/2-inch knockouts.
* Three-pronged power cable. *I recommend getting one that is at least 8 feet*.
* 3 outlets.
* 1 switch.
* 3 1/2-inch cable connectors.
* 16-gauge black wire for the hot wire.
* 16-gauge white wire for the neutral wire.
* 16-gauge green wire for the ground wire.
* 1 Raspberry Pi Zero W.
* 1 5-volt micro-USB power supply.
* 1 5-volt trigger Solid-State Relay board.
* 3 wires to connect the Raspberry Pi Zero W to the Solid-State Relay board.

Luckily, you can purchase most of the required hardware and wiring at your local Lowe's or Home Depot. You can purchase the Raspberry Pi Zero W and Solid-State Relay board online from a variety of vendors, my personal favorite being [Adafruit](https://www.adafruit.com/).

<p align="center">
    <img src="./share/images/ecessary_parts.jpg" width=600>
</p>

Once you have all the parts that you need, it is time to start putting your BYOSO together!

### Step 2: Remove knockouts and connect Outlet Boxes

In order to successfully wire BYOSO, you need to combine the outlet boxes to each other using some spare screws and nuts.

<p align="center">
    <img src="./share/images/connect_box.jpg" width=600>
</p>

Before screwing the two boxes together, you will want to remove all the knockouts on the shared side of the outlet boxes. This is where the wires will pass through between the outlets and switch.

Once you have removed all the knockouts on the shared side, you will want to remove two more knockouts from one box and then remove one more knockout from the other box. The box with the two extra knockouts will contain the main power cord. The other two knockouts will be used to connect the hot wire to the Solid-State Relay.

This is what your outlet boxes should look like once you have connected them to each other:

<p align="center">
    <img src="./share/images/knockouts.jpg" width=600>
</p>

### Step 3: Add Cable Connectors to connected Outlet Boxes

Nothing is worse than unsecured wires! To secure the main power cord and the hot wires that will connect to our Solid-State Relay board, we need to add some cable connectors to our connected box.

<p align="center">
    <img src="./share/images/cable_connector.jpg" width=600>
</p>

Attach the cable connectors to the box by attaching them to the three exposed knockouts. The cable connectors I used come with a nut to secure them in the knockouts, however, you can also use snap-in cable connectors. This is what your box with the cable connectors added:

<p align="center">
    <img src="./share/images/repared_outlet_box.jpg" width=600>
</p>

### Step 4: Prepare Power Cord

Now it is time to add the power cord to your box. **Do not plug in the power cord while you are doing anything with the wires!** Electricution is one of the many things that you will be happy to leave off your bucket list.

That being said, you will want to have three wires exposed on your power cord. One for the hot wire, one for the neutral wire, and another for the ground wire. In my case, I am using a spare European-style power cord that I had lying around. The typical color coding for a three-pronged power wire is the following:

* Black (or Red) -> Hot
* White (or Black) -> Neutral
* Green -> Ground

For the European-style, the color coding is the following:

* Brown -> Hot
* Blue -> Neutral
* Green -> Ground

<p align="center">
    <img src="./share/images/repared_power_cord.jpg" width=600>
</p>

With the three wires exposed, you will want to feed the power cord through the back cable connector. You will want to feed a generous amount so that you will have some wiggle room available while you are connecting the outlets and switch. This is about how much of the power cord you will want to feed through the cable connector:

<p align="center">
    <img src="./share/images/ower_cord.jpg" width=600>
</p>

### Step 5: Prepare Outlets and Switch

Before wiring together the outlets and switch, break off the extra tabs using a pair of pliers.

<p align="center">
    <img src="./share/images/break_tabs.jpg" width=600>
</p>

This is what the outlets and switch should look like with the tabs broken off.

<p align="center">
    <img src="./share/images/repared_outlets_and_switch.jpg" width=600>
</p>

With the tabs removed, connect some pieces of your green wire to the ground terminal (the green screw) of each outlet and switch. We will use the green wires to connect to the ground wire of your power cord.

<p align="center">
    <img src="./share/images/setup_ground_wire.jpg" width=600>
</p>

### Step 6: Connect Ground Wire

To connect together the green wires from the outlets and switch to the ground wire, you will need a medium sized electrical cap.

<p align="center">
    <img src="./share/images/electrical_ca.jpg" width=600>
</p>

Attach the four green wires and ground wire to the electrical cap by screwing on the electrical cap. Once the electrical cap is screwed on, secure it to the wires using some electrical tape.

<p align="center">
    <img src="./share/images/connect_ground.jpg" width=600>
</p>

### Step 7: Connect Neutral Wire

Now we will want to attach the neutral wire to the outlets. First, we will want to attach the neutral wire to the outlet that will be in the same outlet box as the switch. With the neutral wire attached to the neutral terminal (silver screw) of the outlet, attach a piece of white wire to the outlet.

<p align="center">
    <img src="./share/images/eutral_from_power_cord.jpg" width=600>
</p>

With that white wire, connect it to the neutral terminal of the second outlet. Attach other piece of white wire to the second outlet and then connect it to the neutral terminal of the third outlet.

<p align="center">
    <img src="./share/images/connect_neutral_wire.jpg" width=600>
</p>

### Step 8: Connect Hot Wire

Now that we have the neutral wire connected to all the outlets, it is time to start wiring the hot wire. For BYOSO, one outlet will be turned on or off by the physical switch. This outlet will be dedicated to powering the Raspberry Pi Zero W. The other two outlets will be turned on or off by the Solid-State Relay board. The core idea is that the physical switch will function as a master on-off. If you want BYOSO off, just flip the switch. If you want BYOSO on, flip the switch and the Pi will be turned on. The other two outlets will be controlled by the Solid-State Relay, but we will get to that later in this tutorial.

That being said, first connect the hot wire from the main power cord to the common terminal (brass or black colored screw) of the switch.

<p align="center">
    <img src="./share/images/connect_hot_wire_to_switch.jpg" width=600>
</p>

After connecting the hot wire to the common terminal of the switch, connect a piece of black wire to the traveler terminal (gold screw) and connect that black wire to the hot terminal (also a gold screw) to the outlet that is in the same box as the switch. After you have connected that black wire from the switch, connect a second black wire to the outlet and feed it out through the second cable connector in the box. *This wire will later be connected to the Solid-State Relay board*.

<p align="center">
    <img src="./share/images/solid_hot_wire.jpg" width=600>
</p>

Now connect another piece of black wire between the two outlets in the second box. After connecting the two outlets together, connect another black wire to one of the outlets and feed it through the cable connector. *This wire will later be connected to the Solid-State Relay board*.

<p align="center">
    <img src="./share/images/hot_wire.jpg" width=600>
</p>

### Step 9: Add Outlet Box Covers

It is now time to secure the outlet box covers to the outlets and switch. Typically, these covers will come packaged with screws that you can use to attach to the outlets and switch. Use those packaged screws to attach the covers to the outlets and switch.

<p align="center">
    <img src="./share/images/secure_cover.jpg" width=600>
</p>

With the covers attached to the outlets and switch, now secure the covers to the outlet boxes. It will be a snug fit, but with a little elbow greese and a screw driver you will be able to get them on. This is what your box should like once you are done getting the covers on:

<p align="center">
    <img src="./share/images/cover_o.jpg" width=600>
</p>

### Step 10: Test Solid-State Relay and Pi Zero W (Optional)

Before we connect the Raspberry Pi Zero W and Solid-State Relay board to the outlet boxes, we need to verify that the hardware is working first! In the picture below, I am holding the Solid-State Relay board. On one side of the board, there are three terminals:

* DC+ -> Connects to the 5V pin on the Pi's GPIO interface.
* DC- -> Connects to the GND pin on the Pi's GPIO interface.
* CH1 -> Connects to one of the general purpose GPIO pins. *Typically I use pin 17*.

On the other side of the board, there are two terminals:
* AC or DC+ -> Connects to the hot wire coming from the box with the outlet and switch.
* AC or DC- -> Connects to the hot wire coming from the box with two outlets.

<p align="center">
    <img src="./share/images/solid_state_relay.jpg" width=600>
</p>

To test our hardware, we will just need a breadboard, a 5-volt LED, a resistor, the Raspberry Pi Zero W, and the Solid-State Relay board.

<p align="center">
    <img src="./share/images/test_circuit.jpg" width=600>
</p>

To test that the Pi is putting out the 5-volt signal we need (make sure that your Pi is powered on), simply connect the 5-volt wire to the same row as the positive terminal (the longer wire) of the LED. To prevent the LED from burning out, connect one end of the resistor to the same row as the negative terminal (shorter leg) of the LED. Now connect the ground wire from the Pi to the same row as the other end of the resistor. If all is working, you should see the LED light up!

<p align="center">
    <img src="./share/images/light_led.jpg" width=600>
</p>

To test that the Solid-State Relay board is working, we are simply going to try and light up the LED status light on the board. The LED status light will indicate whether or not the Solid-State Relay is open or closed. In order to do this test, **you will need to connect two separate power sources to the Solid-State Relay board**. If all goes well connecting the two separate power sources, you should see the LED status light turn on when the switch is open! *By default, the Solid-State Relay may be set to closed. You can use the GPIO pins on the Raspberry Pi Zero W to open the Solid-State Relay, but I will explain how to do this later*.

<p align="center">
    <img src="./share/images/its_alive.jpg" width=600>
</p>

### Step 11: Connect Solid-State Relay and Raspberry Pi Zero W to Outlet Box

To connect the Solid-State Relay board to the outlet boxes, simply connect the two black wires coming from the boxes to the two-terminal side of the board. Here is a picture for what the board should look like connected to the outlet boxes:

<p align="center">
    <img src="./share/images/connect_to_outlet_box.jpg" width=600>
</p>

With the Solid-State Relay board connected to the outlet boxes, connect the Raspberry Pi Zero W to the three-terminal side of the Solid-State Relay board. The pin mapping should be the following:

* Pin 2 - 5-volt - DC+
* Pin 6 - GND - DC-
* Pin 17 - general purpose - CH1

This is what the Pi should look like connected to the Solid-State Relay board:

<p align="center">
    <img src="./share/images/connect_to_pi.jpg" width=600>
</p>

Now it is time to power on BYOSO! In order to power the Raspberry Pi Zero W, plug the 5-volt power supply into the outlet in the same box as the switch. Flip the the switch on and the Pi should power on! This is what the fully-constructed BYOSO should look like:

<p align="center">
    <img src="./share/images/finished_product.jpg" width=600>
</p>

### Step 12: Setup Flask Web Server on Raspberry Pi Zero W

To interact with BYOSO, we need to build an interface that will allow us open or close the Solid-State Relay. Luckily, this is not too difficult to do with [Flask](https://flask.palletsprojects.com/en/2.0.x/) and [W3.CSS](https://www.w3schools.com/w3css/)!

To create the Flask application you will use to control the Solid-State Relay, you need to connect to the Pi using a service like `ssh`. If you do not know the IP address of your Pi Zero, you can use tools like `ifconfig` or `nmap` to find the IP address of the Pi. Once you connect to the Pi Zero, you will need to install Flask on your Pi:

```bash
pip3 install -U Flask
```

With Flask installed, you are ready to create your application to control the Solid-State Relay. On your Pi, you will want to make the directory `templates`. The `templates` directory is where Flask will look for your HTML files. Inside that templates directory, create two files: `on.html` and `off.html`.

Here is the code that you should use for `on.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Jason C. Nucciarone">
    <meta name="description" content="On switch for build your own smart outlet">
    <title>byoso - On switch</title>

    <!-- Import W3.CSS framework for CSS styling -->
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body>
    <div class="w3-display-middle">
        <div class="w3-container">
            <a class="w3-button w3-round w3-xlarge w3-center w3-green" href="/on">On</a>
        </div>
    </div>
</body>
</html>
```

This is what `on.html` should look like when you open the file in your browser:

<p align="center">
    <img src="./share/images/on_button.png" width=600>
</p>

Here is the code that you should use for `off.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Jason C. Nucciarone">
    <meta name="description" content="Off switch for build your own smart outlet">
    <title>byoso - off switch</title>

    <!-- Import W3.CSS framework for CSS styling -->
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body>
    <div class="w3-display-middle">
        <div class="w3-container">
            <a class="w3-button w3-round w3-xlarge w3-center w3-red" href="/off">Off</a>
        </div>
    </div>
</body>
</html>
```

This is what `off.html` should look like when you open the file in your browser:

<p align="center">
    <img src="./share/images/off_button.png" width=600>
</p>

Now with `on.html` and `off.html` created, go to the directory above the `templates` directory (`cd ..`) and create the file `byoso.py`. Here is the Python code that you will want to put in this file:

```python
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
```

### The finished product!

Once you have finished writing `byoso.py`, use the following command to launch your Flask application:

```bash
python3 byoso.py
```

Now you should be able to navigate to `<your_pi's_ip_address>:5000` in your web browser and see the on button. Plug a light into one of the outlets in the box with the two outlet boxes, and then push the on button. You should then see your light turn on and come to life!

<p align="center">
    <img src="./share/gifs/byoso_in_action.gif">
</p>

**Congratulations**, you have successfully built your own smart outlet! Now go out there and have fun not needing the cloud to control your own smart outlet!

## Copyright and License

Code and tutorial copyright &copy; Jason C. Nucciarone 2021. Code and tutorial files released under the [GNU General Public License version 3](https://www.gnu.org/licenses/gpl-3.0.en.html). For any questions about the copyright or using BYOSO in future work, please contact me at jason@nucci.tech.

## Troubleshooting

If you encounter any issues with building your own smart outlet, or if you have any general questions about BYOSO, then please feel free to open an issue on this repository or contact me at jason@nucci.tech!

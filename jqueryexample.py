# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2014 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

#import Adafruit_BBIO.GPIO as GPIO
import time
from logger.sensor import Sensor
  
def turn_me_on(t):
    GPIO.setup("P8_10", GPIO.OUT)
    GPIO.output("P8_10", GPIO.HIGH)
    time.sleep(t)
    GPIO.output("P8_10", GPIO.LOW)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    #turn_me_on(1)
#    s = Sensor('Forward power', '\%', 1, 'P9_37', .8, .5)
    #turn_me_on(1)
    return jsonify(result=a + b)
    #return jsonify(result=s.get_value())

@app.route('/_get_latest_sensor_values')
def get_latest_sensor_values():
    
    #return jsonify(result=s.get_value())


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
# Importing the packages and the libraries
from flask import Flask
import RPi.GPIO as gpio
import time

app = Flask(__name__)
tf=0.8

# Function to initialise the GPIO channels
def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7,gpio.OUT)
    gpio.setup(11,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(15,gpio.OUT)

# Move rover forward
@app.route('/forward')
def forward():
    init()
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()
    return 'moved forward'

# Pivot rover to the left
@app.route('/pivot_left')
def pivot_left():
    init()
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()
    return 'pivoted left'

# Pivot rover to the right
@app.route('/pivot_right')
def pivot_right():
    init()
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()
    return 'pivoted right'

@app.route('/')
def index():
    return 'Control Rover'

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
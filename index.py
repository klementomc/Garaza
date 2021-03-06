from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

#nastavitve pinov
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("stran.html")

@app.route("/prvic")
def garaza1():
    GPIO.output(7, GPIO.LOW)
    time.sleep(1)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(7, GPIO.LOW)
    return render_template("stran1.html")


@app.route("/drugic")
def garaza2():
    GPIO.output(7, GPIO.LOW)
    time.sleep(1)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(7, GPIO.LOW)
    return render_template("stran2.html")

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)

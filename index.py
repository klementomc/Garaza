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
def garaža1():
    GPIO.output(7, GPIO.LOW)
    time.sleep(1)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(2)
    return render_template("stran1.html")


@app.route("/drugic")
def garaža2():
    GPIO.output(7, GPIO.LOW)
    time.sleep(1)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(2)
    return render_template("stran2.html")

if __name__ == "__main__":
    app.debug = True
    app.run()

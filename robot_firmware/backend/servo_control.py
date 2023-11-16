from flask import Flask, render_template, request
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Servo

factory = PiGPIOFactory()
# Creating Servo variables and include volt info
servo1 = Servo(12, pin_factory=factory) #MG, operating voltage- 4.8-7.2
servo2 = Servo(16, pin_factory=factory) #MG, operating voltage- 4.8-7.2
servo3 = Servo(19, pin_factory=factory) #MG, operating voltage- 4.8-7.2
servo4 = Servo(2, pin_factory= factory) #micro, 4.8 nomial, (3V to 6V DC)

app = Flask(__name__)
app.config['DEBUG'] = True

app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/servo", methods=['POST'])
def servo_control():
    slider1 = request.form.get('slider1')
    slider2 = request.form.get('slider2')
    slider3 = request.form.get('slider3')
    slider4 = request.form.get('slider4')


    if slider1 is not None:
        servo_position_1 = ((float(slider1) / 180) * 2) - 1
        servo1.value = servo_position_1

    if slider2 is not None:
        servo_position_2 = ((float(slider2) / 180) * 2) - 1
        servo2.value = servo_position_2

    if slider3 is not None:
        servo_position_3 = ((float(slider3) / 180) * 2) - 1
        servo3.value = servo_position_3
    
    if slider4 is not None:
        servo_position_4 = ((float(slider3) / 180) * 2) - 1
        servo3.value = servo_position_4
    
    return "OK"


if __name__ == "__main__":
    app.run()

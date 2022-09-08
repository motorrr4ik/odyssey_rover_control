import RPi.GPIO as GPIO
from math import copysign
from time import sleep

class Motor:
    
    def __init__(self, en1:int, en2:int, enable:int, freq:int):
        self.en1 = en1
        self.en2 = en2
        self.enable = enable
        self.duty_cycle = 0
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.en1, GPIO.OUT)
        GPIO.setup(self.en2, GPIO.OUT)
        GPIO.setup(self.enable, GPIO.OUT)
        
        self.pwm_en1 = GPIO.PWM(self.en1, freq)
        self.pwm_en2 = GPIO.PWM(self.en2, freq)
        self.pwm_en1.start(0)
        self.pwm_en2.start(0)

    def enable_motor(self):
        GPIO.output(self.enable, GPIO.HIGH)
        print("Motor enabled")

    def disable_motor(self):
        GPIO.output(self.enable, GPIO.LOW)

    def set_dc(self, duty_cycle:int):
       #self.move_forward(duty_cycle)

       if duty_cycle <= 0:
           self.move_backward(abs(duty_cycle))
       elif duty_cycle > 1:
           self.move_forward(abs(duty_cycle))
    
    def move_forward(self, duty_cycle:int):
        self.pwm_en1.ChangeDutyCycle(duty_cycle)
        self.pwm_en2.ChangeDutyCycle(0)

    def move_backward(self, duty_cycle:int):
        self.pwm_en1.ChangeDutyCycle(0)
        self.pwm_en2.ChangeDutyCycle(duty_cycle)
    
    def get_pins(self):
        print("en1 : " + str(self.en1) + " en2 : " + str(self.en2) + " enable : " + str(self.enable))
    
    def __del__():
        GPIO.setup(self.en1, GPIO.IN)
        GPIO.setup(self.en2, GPIO.IN)
        GPIO.setup(self.enable, GPIO.IN)
        self.pwm_en1.stop()
        self.pwm_en2.stop()
        GPIO.cleanup()



if __name__ == '__main__':
    motor = Motor(27, 10, 19, 100)
    motor.get_pins()
    motor.enable_motor()
    motor.set_dc(-50)

    sleep(5)
    motor.set_dc(0)


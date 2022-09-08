import RPi.GPIO as GPIO
from threading import Thread
from time import sleep
from motor import Motor
import random

class Rover(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.name = "odyssey"
        self.dc_right = 0
        self.dc_left = 0
        #self.right_motor = Motor(27, 10, 19, 100)
        #self.left_motor = Motor(24, 18, 26, 100)
    
    def init_left_motor(self, en1:int, en2:int, enable:int):
        self.left_motor = Motor(en1, en2, enable, 100)
        self.left_motor.enable_motor()

    def init_right_motor(self, en1:int, en2:int, enable:int):
        self.right_motor = Motor(en1, en2, enable, 100)
        self.right_motor.enable_motor()
    
    def disable_motors():
        self.right_motor.disable_motor()
        self.left_motor.disable_motor()

    def to_string(self):
        print(self.name)
    
    def get_right_motors_pins(self):
        print("en_1 : " + str(self.en1_right) + " " + "en_2 : " + str(self.en2_right) + "  " + "enable : " + str(self.enable_right))

    def set_right_dc(self, new_right_dc:int):
        self.dc_right = new_right_dc

    def set_left_dc(self, new_left_dc:int):
        self.dc_left = new_left_dc
    

    def run(self):
        while(1):
            self.right_motor.set_dc(self.dc_right)
            self.left_motor.set_dc(self.dc_left)
            print("Here\n") 
    

        
if __name__ == "__main__":
    rover = Rover()
    rover.to_string()
    rover.init_right_motor(27, 10, 19)
    rover.init_left_motor(24, 18, 26)
    rover.start()
    try:

        while(1):
            # get data from camera
            rover.set_left_dc(50)
            rover.set_right_dc(50)
            sleep(2)
            rover.set_left_dc(85)
            rover.set_right_dc(85)
            sleep(2)
    except KeyboardInterrupt:
        rover.set_left_dc(0)
        rover.set_right_dc(0)
        rover.disable_motors()
    #rover.move_rover.set_rigrover.set_right_dc(50) ht_dc(50) right_motors_forward()
    #sleep(5)
    #rover.stop_motors()


#Njane Alvin
#09.03.2026
# Program to show drone flight

from pysimverse import Drone

import time

# Instance of flight

drone= Drone(speed= 1000)
drone.connect()
drone.take_off(3)

drone.move_forward(100)
time.sleep(0.01)

drone.move_left(290)

time.sleep(0.1)
drone.move_forward(100)
time.sleep(0.01)

drone.move_right(300)

time.sleep(0.1)
drone.move_forward(150)
time.sleep(0.01)

drone.move_right(300)
time.sleep(0.1)
drone.land

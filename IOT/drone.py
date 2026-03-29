# Square Flight Path in PySimVerse

from Pysimverse import Drone
import time


def main():

    # Create drone object
    drone = Drone()

    # Connect to simulator
    drone.connect()

    print("Taking off...")
    drone.take_off()

    time.sleep(3)

    # Fly in square
    for i in range(4):

        print("Flying side", i + 1)

        drone.move_forward(5)
        time.sleep(2)

        drone.rotate(90)
        time.sleep(2)

    # Land drone
    print("Landing...")
    drone.land()

    print("Square flight complete!")


if __name__ == "__main__":
    main()
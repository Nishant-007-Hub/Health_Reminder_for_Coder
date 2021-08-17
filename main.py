from time import time
from playsound import playsound
import datetime
import multiprocessing

def log_(msg):
    with open("mylogs.txt", 'a')as f:
        f.write(f"{msg}{datetime.datetime.now()}\n")


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()

    watersec = 30 * 60
    eyesec = 20 * 60
    exercisesec = 40 * 60

    while True:
        if time() - init_water > watersec:
            print("water drinking time...")
            log_("water done at::\t")
            var = multiprocessing.Process(target=playsound, args=("water.mp3",))
            var.start()
            input("Enter any key to stop\n")
            var.terminate()
            init_water = time()

        if time() - init_eyes > eyesec:
            print("Eyes Exercise time...")
            log_("done Eyes at::\t")
            var = multiprocessing.Process(target=playsound, args=("eyes.mp3",))
            var.start()
            input("Enter any key to stop\n")
            var.terminate()
            init_eyes = time()

        if time() - init_exercise > exercisesec:
            print("Physical Exercise time...")
            log_("done Exercise at::\t")
            var = multiprocessing.Process(target=playsound, args=("exercise.mp3",))
            var.start()
            input("Enter any key to stop\n")
            var.terminate()
            init_exercise = time()

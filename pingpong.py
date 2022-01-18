import os
import time
import pynput


def draw():
    pass


def moveBall():
    pass


def on_press():
    pass


def on_release(key):
    pass


pynput.keyboard.Listener(
    on_press=on_press,
    on_release=on_release
).start()

while True:
    os.system('cls')
    draw()
    moveBall()
    time.sleep(0.1)

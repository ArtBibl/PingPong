import os
import time
import pynput

WIDTH = 50
HEIGHT = 20
ballX = 1
ballY = 1
rocket1 = 3
rocket2 = 4
rocketLenght = 5
dirX = 1
dirY = 1


def moveBall():
    global ballX, ballY, dirY, dirX
    ballX += dirX
    ballY += dirY
    if ballY == HEIGHT - 1 or ballY == 0:
        dirY *= -1
    if ballX == WIDTH - 1 and ballY >= rocket2 and ballY < rocket2 + rocketLenght:
        dirX *= -1
    if ballX == WIDTH - 1 and ballY >= rocket1 and ballY < rocket1 + rocketLenght:
        dirX *= -1

def draw():
    y = 0
    while y < HEIGHT:
        x = 0
        result = ''
        while x < WIDTH:
            if x == ballX and y == ballY:
                result += 'O'
            elif x == 0 and y >= rocket1 and y < rocket1 + rocketLenght:
                result += '|'
            elif x == WIDTH - 1 and y >= rocket2 and y < rocket2 + rocketLenght:
                result += '|'
            else:
                result += '-'
            x += 1
        print(result)
        y += 1


def on_press(key):
    global rocket2, rocket1
    if key == pynput.keyboard.Key.up:
        rocket2 -= 1
    if key == pynput.keyboard.Key.down:
        rocket2 += 1
    if key == pynput.keyboard.Key.shift:
        rocket1 -= 1
    if key == pynput.keyboard.Key.cnt:
        rocket1 += 1
        print(rocket1)


def on_release(key):
    pass


pynput.keyboard.Listener(
    on_press=on_press,
    on_release=on_release
).start()

while True:
    os.system('cls')
    print('*' * WIDTH)
    draw()
    moveBall()
    print('*' * WIDTH)
    time.sleep(0.1)

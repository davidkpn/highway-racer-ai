'''

https://www.crazygames.com/game/highway-racer


'''
from threading import Thread
import numpy as np
import cv2
import time
from direct_keys import PressKey,ReleaseKey, W, A, S, D
from alexnet import alexnet
from get_keys import key_check

import random
import mss

WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 50
MODEL_NAME = 'pyhighway-racer-{}-{}-{}-epochs-64K-data.model'.format(LR, 'alexnetv2',EPOCHS)

# Implement a human click by delaying the press time.
human_time = 0.09
KEYS = [W,A,S,D]
def make_move(prediction):
    for index, key in enumerate(KEYS):
        if prediction[index] > .5:
            PressKey(key)
    time.sleep(human_time)
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(S)
    ReleaseKey(D)

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

def main():
    last_time = time.time()
    print("Ai start playing in..")
    for i in list(range(1,4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    monitor = {"top": 410, "left": 410, "width": 1000, "height": 300}
    with mss.mss() as sct:
        while(True):

            if not paused:
                screen = np.array(sct.grab(monitor))
                print('fps: {}'.format(1/ (time.time()-last_time)))
                last_time = time.time()
                # screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                screen = cv2.resize(screen, (160,120))

                prediction = model.predict([screen.reshape(160,120,1)])[0]

                Thread(target=make_move, args=[prediction]).start()

            keys = key_check()

            # P = Pause, Q = Quit
            if 'P' in keys:
                if paused:
                    paused = False
                    time.sleep(1)
                else:
                    paused = True
                    ReleaseKey(A)
                    ReleaseKey(W)
                    ReleaseKey(D)
                    ReleaseKey(S)
                    time.sleep(1)
            elif 'Q' in keys:
                break

main()

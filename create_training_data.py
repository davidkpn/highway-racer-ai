# create_training_data.py
'''
Create the training data by recording [frame,keys].
on second run will load the previous data and continue recording.
'''
import numpy as np
import cv2
import time
from get_keys import key_check
import os
import mss


def keys_to_output(keys):
    '''
    Convert keys to a multi-hot-key vector
    [W,A,S,D] boolean values.
    '''
    output = [0,0,0,0]
    if 'W' in keys:
        output[0] = 1
    if 'A' in keys:
        output[1] = 1
    if 'S' in keys:
        output[2] = 1
    if 'D' in keys:
        output[3] = 1
    if len(keys) == 0:
        output[0] = 1
    return output


file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name, allow_pickle=True))
else:
    print('File does not exist, starting fresh!')
    training_data = []


def main():
    print("Start recording game, in..")
    for i in list(range(1,4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False

    monitor = {"top": 410, "left": 410, "width": 1000, "height": 300}
    with mss.mss() as sct:
        while(True):
            if not paused:
                # Capture the game location on screen ( individual for 1920:1080 resolution)
                screen = np.array(sct.grab(monitor))
                # screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                screen = cv2.resize(screen, (160,120))
                keys = key_check()
                output = keys_to_output(keys)
                training_data.append([screen,output])

                if len(training_data) % 500 == 0:
                    print(len(training_data))
                    np.save(file_name,training_data)

            keys = key_check()
            if 'P' in keys:
                if paused:
                    paused = False
                    print('unpaused!')
                    time.sleep(1)
                else:
                    print('Pausing!')
                    paused = True
                    time.sleep(1)


main()

import cv2
import mss
import numpy as np
import pyautogui
from time import sleep, time


def grab(bbox):
    img = np.array(sct.grab(bbox))
    binary = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    cv2.imshow('image', binary)

    cactus = binary[-1,:]
    bird = binary[1,:]

    sum_cactus = np.sum(cactus)
    sum_bird = np.sum(bird)
    return sum_cactus, sum_bird

def press_up(time):
    pyautogui.keyDown('up')
    sleep(time)
    pyautogui.press('down')


with mss.mss() as sct:

    total_time = 0
    bbox = {"top": 334, "left": 260, "width": 85, "height": 40}
    flag = 1
    val = 20995
    
    while True:
        cur_time = time()
        sum_cactus, sum_bird = grab(bbox)
        # print(sum_cactus)
        if sum_cactus < val:
            # print(total_time)
            if total_time >= 20.0:
                press_up(0.09)
                # print('jump > 20')
            # elif total_time >= 30.0:
            #     press_up(0.06)
            #     print('jump > 30')
            else:
                pyautogui.keyDown('up')

        if sum_bird < val:
            flag = 1
            pyautogui.keyDown('down')
            sleep(0.25)

        if sum_bird == val and flag == 1:
            flag = 0
            pyautogui.keyUp('down')

        
        total_time += time() - cur_time
        
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
import cv2
import mss
import numpy as np
import pyautogui
from time import sleep
import matplotlib.pyplot as plt

def grab(bbox):
    img = np.array(sct.grab(bbox))
    # binary = np.sum(img, 2)
    # binary[binary > 0] = 1
    binary = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    # cv2.imshow('image', cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))
    cv2.imshow('image', binary)

    # cnt_black_pxl = np.sum(img < 100)
    # cnt_white_pxl = np.sum(img > 100)
    # a = sum(map(sum, binary))
    cactus = binary[40,:]
    bird = binary[3,:]
    # cactus = img[45,:,0]
    # bird = img[5,:,0]

    sum_cactus = np.sum(cactus)
    sum_bird = np.sum(bird)
    # print(sum_cactus)

    return sum_cactus, sum_bird

def press_up():
    pyautogui.keyDown('space')
    sleep(0.001)
    pyautogui.keyUp('space')
    sleep(0.001)
    # pyautogui.press('down')
    # pyautogui.keyUp('down')
    # pyautogui.keyDown('space')
    # time.sleep(0.13)
    # pyautogui.keyUp('space')
    # pyautogui.keyDown('down')

with mss.mss() as sct:
    bbox = {"top": 330, "left": 285, "width": 70, "height": 50}
    flag = 1
    val = 17290
    while True:
        
        sum_cactus, sum_bird = grab(bbox)
        # print(sum_cactus)
        if sum_cactus < val:
            # press_up()
            pyautogui.keyDown('up')      
            sleep(0.01)             
            # pyautogui.keyUp('space')
        # if sum_cactus == val:
        #     pyautogui.keyUp('up')
            # pyautogui.press('down')

        if sum_bird < val:
            # pyautogui.press('down')
            # print(bird)
            print(sum_bird)
            flag = 1
            pyautogui.keyDown('down')
            sleep(0.5)
            # pyautogui.keyUp('down')

        if sum_bird == val and flag == 1:
            pyautogui.keyUp('down')
            flag = 0
            print('flag')
            print(sum_bird)
        

        #light mode
        # if cnt_black_pxl > 500 and cnt_black_pxl < 5000:
        #     pyautogui.press('up')

        # if cnt_white_pxl > 500 and cnt_white_pxl < 10000:
        #     pyautogui.press('up')

        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
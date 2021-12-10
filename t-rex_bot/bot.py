qimport cv2
import mss
import numpy as np
import pyautogui
import time
import matplotlib.pyplot as plt

def press_space():
    pass
    # pyautogui.press('down')
    # pyautogui.keyUp('down')
    # pyautogui.keyDown('space')
    # time.sleep(0.13)
    # pyautogui.keyUp('space')
    # pyautogui.keyDown('down')

with mss.mss() as sct:
    bbox = {"top": 325, "left": 250, "width": 120, "height": 65}
    flag = 1
    val = 29640
    while True:
        img = np.array(sct.grab(bbox))
        # cv2.imshow('image', cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        # cnt_black_pxl = np.sum(img < 100)
        # cnt_white_pxl = np.sum(img > 100)
       

        cactus = img[45,:,0]
        bird = img[3,:,0]
        print(cactus)
        print(bird)

        # plt.subplot(121)
        # plt.imshow(cactus)
        # plt.subplot(122)
        # plt.imshow(bird)
        # plt.show()

        sum_cactus = np.sum(cactus)
        sum_bird = np.sum(bird)
        # print(sum_cactus)

        if sum_cactus < val:
            pyautogui.press('up')
        if sum_bird < val:
            pyautogui.press('down')
            # print(bird)
            print(sum_bird)
            flag = 1
        if sum_bird and flag == 1:
            pyautogui.keyUp('down')
            flag = 0
        

        #light mode
        # if cnt_black_pxl > 500 and cnt_black_pxl < 5000:
        #     pyautogui.press('up')

        # if cnt_white_pxl > 500 and cnt_white_pxl < 10000:
        #     pyautogui.press('up')

        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
import cv2
import numpy as np

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("Cnts", cv2.WINDOW_KEEPRATIO)

background = None

while cam.isOpened():
    _, image = cam.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (11, 11), 0)
    # mask = cv2.inRange(gray, (200), (255))
    # mask = cv2.erode(mask, None, iterations=2)
    # mask = cv2.dilate(mask, None, iterations=2)
    cnts = cv2.Canny(gray, 200, 250)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('b'):
        background = gray.copy()

    if background is not None:
        delta = cv2.absdiff(background, gray)
        thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
            
    cv2.imshow("Cnts", cnts)
    cv2.imshow("Camera", image)
    
cam.release()
cv2.destroyAllWindows
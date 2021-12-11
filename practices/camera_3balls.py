import cv2
import numpy as np
import time
# green 29 50 130
# blue 10 102 142
# red 5 70 205

cam = cv2.VideoCapture(1)
cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)

lowerGreen = (44, 100, 150)
upperGreen = (85, 255, 255)
lowerRed = (20, 60, 100)
upperRed = (45, 255, 255)
lowerBlue = (85, 230, 110)
upperBlue = (130, 255, 255)

maskLower = [lowerRed, lowerGreen, lowerBlue]
maskUpper = [upperRed, upperGreen, upperBlue]

# colors = ['green', 'blue', 'yellow']
center_balls = []

while cam.isOpened():
    _, image = cam.read()
    image = cv2.flip(image, 1)
    curr_time = time.time()
    blurred = cv2.GaussianBlur(image, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    for i in range(len(maskUpper)):
        mask = cv2.inRange(hsv, maskLower[i], maskUpper[i])
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            (curr_x, curr_y), radius = cv2.minEnclosingCircle(c)
            center_balls.append((curr_x, curr_y))
            if radius > 10:
                cv2.circle(image, (int(curr_x), int(curr_y)), int(radius), (0, 255, 255), 2)
                cv2.circle(image, (int(curr_x), int(curr_y)), 5, (0, 255, 255), 2)

    
    # cv2.putText(image, center_balls, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 117), 2)
    cv2.imshow("Camera", image)
    # cv2.imshow("Camera", mask)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
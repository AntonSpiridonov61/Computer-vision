import cv2
import numpy as np
import time
# green 29 50 130
# blue 10 102 142
# red 5 70 205

cam = cv2.VideoCapture(1)
cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)

lower = (44, 100, 150)
upper = (90, 255, 255)

prev_time = time.time() 
curr_time = time.time() 
prev_x, prev_y = 0, 0
curr_x, curr_y = 0, 0
d = 5.6e-2
radius = 1
max_speed = 0.0


while cam.isOpened():
    _, image = cam.read()
    image = cv2.flip(image, 1)
    curr_time = time.time()
    blurred = cv2.GaussianBlur(image, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)


    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        (curr_x, curr_y), radius = cv2.minEnclosingCircle(c)
        if radius > 10:
            cv2.circle(image, (int(curr_x), int(curr_y)), int(radius), (0, 255, 255), 2)
            cv2.circle(image, (int(curr_x), int(curr_y)), 5, (0, 255, 255), 2)
    time_diff = curr_time - prev_time
    pxl_per_m = d / radius
    dist = ((prev_x - curr_x) ** 2 + (prev_y - curr_y) ** 2) ** 0.5
    speed = dist / time_diff * pxl_per_m 
    if speed > max_speed:
        max_speed = speed
    cv2.putText(image, "Speed = {0:.5f}m/s".format(max_speed), 
                (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 117), 2)
    cv2.imshow("Camera", image)
    # cv2.imshow("Camera", mask)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    prev_time = curr_time
    prev_x = curr_x
    prev_y = curr_y

cam.release()
cv2.destroyAllWindows()
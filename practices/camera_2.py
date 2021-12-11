import cv2
import numpy as np

cam = cv2.VideoCapture(1)
cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("Background", cv2.WINDOW_KEEPRATIO)

roi = None
cnt_frames = 0 
while cam.isOpened():
    _, image = cam.read()
    cnt_frames += 1
    image = cv2.flip(image, 1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if roi is not None:
        res = cv2.matchTemplate(gray, roi, cv2.TM_CCORR_NORMED)
        # cv2.imshow("match template", res)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + roi.shape[1], top_left[1] + roi.shape[0])
        cv2.rectangle(image, top_left, bottom_right, 255, 2)

    cv2.imshow("Camera", image)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('r'):
        r = cv2.selectROI("ROI selection", gray)
        roi = gray[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
        cv2.imshow("ROI", roi)
        cv2.destroyWindow("ROI selection")

cam.release()
cv2.destroyAllWindows()
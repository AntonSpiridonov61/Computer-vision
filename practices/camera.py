import cv2
import numpy as np

cam = cv2.VideoCapture(1)
cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("Background", cv2.WINDOW_KEEPRATIO)

background = None
prev_gray = None
buffer = []
cnt_frames = 0 
while cam.isOpened():
    ret, image = cam.read()
    cnt_frames += 1
    image = cv2.flip(image, 1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (71, 71), 0)
    key = cv2.waitKey(1)
    if cnt_frames % 20 == 0:
        if prev_gray is not None:
            diff = prev_gray - gray
            buffer.append(diff.mean())
    if len(buffer) > 6:
        buffer.pop(0)
        std = np.std(buffer)
        if std < 50:
            print(std)
            print("update_back")
            background = gray.copy()
            buffer.clear()
            
    if key == ord('q'):
        break

    if key == ord('b'):
        background = gray.copy()

    if background is not None:
        delta = cv2.absdiff(background, gray)
        thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Background", image)
    cv2.imshow("Camera", image)
    prev_gray = gray


cam.release()
cv2.destroyAllWindows()
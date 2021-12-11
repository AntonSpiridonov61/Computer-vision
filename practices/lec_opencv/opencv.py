import cv2
import numpy as np

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    raise RuntimeError('we')

ret, cheb = cam.read()

news = cv2.imread("lec_opencv/source/news.jpg")
cheb = cv2.imread("lec_opencv/source/cheburashka.jpg")
#cheb = cv2.resize(cheb, (cheb.shape[0]//2, cheb.shape[1]//2))
rows, cols, _ = cheb.shape
pts1 = np.float32([[0,0], [0, rows], [cols, 0], [cols, rows]])
pts2 = np.float32([[18, 24], [39, 297], [435, 51], [435, 270]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

aff_img = cv2.warpPerspective(cheb, matrix, (cols, rows))
aff_img = aff_img[:-150, :-150]
gray = cv2.cvtColor(aff_img, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

roi = news[:aff_img.shape[0], :aff_img.shape[1]]
mask_inv = cv2.bitwise_not(mask)

bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
# fg = cv2.bitwise_and(cheb, cheb, mask=mask)
image = cv2.add(aff_img, bg)
news[:image.shape[0], :image.shape[1]] = image

cv2.namedWindow("Image")
cv2.imshow("Image", news)
cv2.waitKey(0)
cv2.destroyAllWindows()
cam.release()

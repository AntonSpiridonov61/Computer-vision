import cv2

cat = cv2.imread('cat/cat.png')
cat1 = cv2.cvtColor(cat, cv2.COLOR_BGR2GRAY)
cat2 = cv2.imread('cat/cat2.png', 0)

diff = cv2.absdiff(cat1, cat2)

thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.dilate(thresh, None, iterations=2)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    (x, y, w, h) = cv2.boundingRect(cnt)
    cv2.rectangle(cat, (x, y), (x+w, y+h), (0, 0, 255), 2) 

cv2.putText(cat, f"Differences = {len(contours)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0))

cv2.namedWindow("original", cv2.WINDOW_KEEPRATIO)
# cv2.namedWindow("original", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("difference", cv2.WINDOW_KEEPRATIO)

cv2.imshow("original", cat)
cv2.imshow("difference", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
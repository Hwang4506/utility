import sys
print(sys.executable)
import cv2

img = cv2.imread("/data/y8_3/test.png")

cv2.imshow("test", img)
cv2.waitKey(0)
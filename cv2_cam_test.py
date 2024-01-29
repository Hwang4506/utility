import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cap.isOpened():
    _, frame = cap.read()

    cv2.imshow("res",frame)

    if cv2.waitKey(32) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
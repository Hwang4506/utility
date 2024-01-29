import cv2
import datetime
import base64
import sys

# cap = cv2.VideoCapture(1) # 기본 640*480
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while (True):

    grabbed, frame = cap.read()
    cv2.imshow('Original Video', frame)

    key = cv2.waitKey(1);
    if key == ord('q'):
        break
    elif key == ord('s'):
        retval, image = cap.read()  # 이미지 캡쳐
        # Convert captured image to JPG
        retval, buffer = cv2.imencode('.jpg', image) 
        # Convert to base64 encoding and show start of data
        jpg_as_text = base64.b64encode(buffer)
        # print(jpg_as_text)
        # print(type(jpg_as_text))
        print(sys.getsizeof(jpg_as_text))
        # Convert back to binary
        jpg_original = base64.b64decode(jpg_as_text)
        # print(type(jpg_original))
        # Write to a file to show conversion worked
        with open("C:\\Users\\dydrm\\Desktop\\test\\" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f") + '.jpg', 'wb') as f_output:
            f_output.write(jpg_original)

cap.release()
cv2.destroyAllWindows()
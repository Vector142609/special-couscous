from unittest import result
import cv2

def take_snapshot():
    videoCapturedObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCapturedObject.read()
        cv2.imwrite("Picture1.png",frame)
        result = False


    videoCapturedObject.release()

    cv2.destroyAllWindows()

take_snapshot()
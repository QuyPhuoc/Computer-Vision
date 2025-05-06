import cv2
import matplotlib.pyplot as plt

video = cv2.VideoCapture(r'/home/phuoc/Image/Cook.mp4')

while True:
    ret, frame = video.read()
    if ret:
        cv2.imshow('Video', frame)
        if cv2.waitKey(25) == ord('x'):
            cv2.imwrite(r'/home/phuoc/Image/nau.jpg', frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            Erosion = cv2.medianBlur(gray, 3)
            Dilation = cv2.convertScaleAbs(gray, 1, 5)
            cv2.imwrite(r'/home/phuoc/Image/Erosion.jpg', Erosion)
            cv2.imwrite(r'/home/phuoc/Image/Dilation.jpg', Dilation)
        if cv2.waitKey(25) == ord('q'):
            break
video.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

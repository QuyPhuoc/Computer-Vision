import cv2
from numpy.random import laplace

video = cv2.VideoCapture(r'C:\Anhdep\Cook.mp4')
while True:
    ret, frame = video.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(25) == ord('x'):
        #Chuyen doi ve anh gausss
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # gauss = cv2.GaussianBlur(gray, (5,5), 7)
        #Laplace
        new = cv2.Laplacian(gray, cv2.CV_64F, ksize=3)
        res = cv2.convertScaleAbs(new)
        cv2.imwrite(r'laplace.jpg', res)
    if cv2.waitKey(25) == ord('q'): break
video.release()
cv2.destroyAllWindows()

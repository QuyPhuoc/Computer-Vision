import cv2
import numpy
import numpy as np

img = cv2.imread(r'C:\Anhdep\1.jpg')
cv2.namedWindow('Hoa')
h, w = img.shape[:2]
x = 0
def get_X(pos):
    global x
    x = -pos

def get_Y(pos):
    global x
    x = pos
#Tao trackbar
cv2.createTrackbar('X', 'Hoa', x, h, get_X)
cv2.createTrackbar('Y', 'Hoa', x, h, get_Y)
while True:
    new = np.float32([[1, 0, 1],[0,1,x]])
    tran1 = cv2.warpAffine(img, new, (w,h))
    cv2.imshow('Hoa', tran1)
    if cv2.waitKey(25) == ord('x'):
        break

cv2.destroyAllWindows()


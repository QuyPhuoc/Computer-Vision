import cv2
import numpy as np

img = cv2.imread(r'C:\Anhdep\1.jpg')
cv2.namedWindow('Hoa hong')
h,w = img.shape[:2]
tX = 0
tY = 0

def get_tX(pos):
    global tX
    tX = pos

def get_tY(pos):
    global tY
    tY = pos

cv2.createTrackbar('XY', 'Hoa hong', 0, 200, get_tX)
cv2.createTrackbar('YX', 'Hoa hong', 0, 200, get_tY)

while True:
    M1 = np.float32([[1,0,tX], [0, 1, tY]])
    trans = cv2.warpAffine(img, M1, (w, h))
    cv2.imshow('Hoa hong', trans)
    if cv2.waitKey(20) == ord('q'): break

cv2.waitKey(0)
cv2.destroyAllWindows()
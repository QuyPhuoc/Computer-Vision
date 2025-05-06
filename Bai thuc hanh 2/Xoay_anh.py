import cv2
import numpy as np

img = cv2.imread(r'/home/phuoc/Anhdep/1.jpg')
cv2.namedWindow('Hoa hong')
h,w = img.shape[:2]
tX = 0

# M = np.float32([[1, 0, tx],[0, 1, ty]])
def get_tX(pos):
    global tX
    tX = pos

cv2.createTrackbar('XY', 'Hoa hong', 0, 360, get_tX)

while True:
    M = cv2.getRotationMatrix2D((w//2, h//2), tX, 0.7)
    res = cv2.warpAffine(img, M, (w,h))
    cv2.imshow('hoa hong', res)
    if cv2.waitKey(20) == ord('q'): break

cv2.imshow('Anh moi', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
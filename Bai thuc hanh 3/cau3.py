import cv2
import numpy as np
img = cv2.imread(r'C:\Anhdep\coco.jpg')
cv2.resize(img, None, fx = 8, fy = 8)
cv2.namedWindow('Anh dep')
h,w = img.shape[:2]

X = 0
# Gọi hàm với img.shape[1] để lấy chiều rộng
def get_X_Y(pos):
    global X
    X = pos - img.shape[1]

#Tạo trackbar
cv2.createTrackbar('Dich anh', 'Anh dep', img.shape[1], img.shape[1] * 2, get_X_Y)
while True:
    M1 = np.float32([[1, 0, X], [0, 1, 0]])
    trans = cv2.warpAffine(img, M1, (w, h))
    cv2.imshow('Anh dep', trans)
    if cv2.waitKey(20) == ord('q'): break

cv2.destroyAllWindows()
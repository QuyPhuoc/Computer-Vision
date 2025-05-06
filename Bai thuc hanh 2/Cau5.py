import cv2
import numpy as np
img = cv2.imread(r'C:\Anhdep\1.jpg')
h,w = img.shape[:2]
#Nhập vào bàn phím
x = float(input('Nhap goc xoay x: '))
#Hàm xoay ảnh
M = cv2.getRotationMatrix2D((0,0), x, 1)
img_new = cv2.warpAffine(img, M, (w,h))
cv2.imshow('New', img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

img = cv2.imread(r'/home/phuoc/Anhdep/1.jpg')
h,w = img.shape[:2]
tx = float(input('Nhap gia tri tx: '))
ty = float(input('Nhap gia tri ty: '))

#Hàm dịch ảnh
M = np.float32([[1,0,tx], [0,1,ty]])
warpAffine = cv2.warpAffine(img, M, (w, h))
cv2.imshow('Anh moi', warpAffine)
cv2.waitKey(0)
cv2.destroyAllWindows()
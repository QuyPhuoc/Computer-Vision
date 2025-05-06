import cv2
import numpy as np

img = cv2.imread(r'/home/phuoc/Anhdep/1.jpg')
h,w = img.shape[:2]
tx,ty = 100, -100

M = np.float32([[1, 0, tx],[0, 1, ty]])
res = cv2.warpAffine(img, M, (w,h))

cv2.imshow('Anh moi', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
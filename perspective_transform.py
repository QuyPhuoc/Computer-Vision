import cv2
import numpy as np

img = cv2.imread(r'C:\Anhdep\sach.jpg')
arr1 = np.float32([[670,872],[1441,859],[490,2137],[1441,2217]])
w,h = [600, 600]
arr2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
M = cv2.getPerspectiveTransform(arr1, arr2)
img_new = cv2.warpPerspective(img, M, (w,h))
# cv2.imshow('Sach', img)
cv2.imshow('NEW', img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

img = cv2.imread(r'C:\Anhdep\anh-mo-ta.png')
img = cv2.resize(img, None, fx=0.5, fy=0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Tách biên hoặc phân ngưỡng trước khi co, giãn
ret, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5), dtype=np.uint8)
open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Anh',img)
cv2.imshow('Thresh', thresh)
cv2.imshow('OPEN', open)
cv2.imshow('CLOSE', close)
cv2.waitKey(0)
cv2.destroyAllWindows()
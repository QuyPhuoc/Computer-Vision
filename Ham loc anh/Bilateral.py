import cv2

img = cv2.imread(r'C:\Anhdep\trump.jpg')
img_new = cv2.bilateralFilter(img, 9, 50, 50)

cv2.imshow('Anh dep', img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
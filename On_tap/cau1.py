import cv2

img = cv2.imread(r'C:\Anhdep\1.jpg')
cv2.imshow('Anh dep', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
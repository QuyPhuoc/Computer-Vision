import cv2

img = cv2.imread(r'C:\Anhdep\1.jpg')
cv2.imshow('New', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
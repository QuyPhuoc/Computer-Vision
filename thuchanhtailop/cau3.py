import cv2

img = cv2.imread(r'C:\Anhdep\1.jpg')
img_new = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('New', img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()

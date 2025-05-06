import cv2

img = cv2.imread(r'C:\Anhdep\trump.jpg')

img_new = cv2.GaussianBlur(img, (5,5), 11)
cv2.imshow('New', img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
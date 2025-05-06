import cv2

img = cv2.imread(r'C:\Anhdep\coco.jpg')
cv2.resize(img, None, fx=3, fy=3)
gauss = cv2.GaussianBlur(img, (5,5), 7)
res = cv2.Canny(gauss, 50, 100)

cv2.imshow('New', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
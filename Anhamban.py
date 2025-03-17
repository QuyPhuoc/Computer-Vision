import cv2
img = cv2.imread(r'C:\Anhdep\1.jpg')
h, w = img.shape[:2]
# new = 255 - img
# cv2.imshow('Anh am ban', new)
crop = img[0:h, 0:w//2]
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('Anh goc', img)
cv2.imshow('Anh da cat', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
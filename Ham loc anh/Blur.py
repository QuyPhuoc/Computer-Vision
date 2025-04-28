import cv2

img = cv2.imread(r'C:\Anhdep\trump.jpg')
# Bộ lọc trung bình: img_blur = cv2.blur(img, (ksize,ksize))
img_new = cv2.blur(img, (5,5))
cv2.imshow('New', img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
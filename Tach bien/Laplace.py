import cv2

img = cv2.imread(r'C:\Anhdep\trump.jpg')

#Chuyển đổi ảnh xám
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Sử dụng bộ lọc
gauss = cv2.GaussianBlur(gray_img, (5,5), 7)
#Áp dụng toán tử Laplace
new = cv2.Laplacian(gauss, cv2.CV_64F, ksize=3)

cv2.imshow('New', new)
cv2.waitKey(0)
cv2.destroyAllWindows()
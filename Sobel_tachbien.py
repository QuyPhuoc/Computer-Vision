import cv2

img = cv2.imread(r'C:\Anhdep\trump.jpg')

#Chuyển đổi ảnh màu sang ảnh xám
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#khử nhiễu
gauss = cv2.GaussianBlur(gray_img, (5,5), 7)

#Áp dụng Sobel
grad_x = cv2.Sobel(gauss, cv2.CV_64F,1, 0, ksize=3)
grad_y = cv2.Sobel(gauss, cv2.CV_64F, 0, 1, ksize=3)

#Lấy giá trị tuyệt đối
abs_grad_x = cv2.convertScaleAbs(grad_x)
abs_grad_y = cv2.convertScaleAbs(grad_y)

#Tính trọng số của 2 mảng (2 ảnh)
grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
cv2.imshow('Anh moi', grad)

cv2.waitKey(0)
cv2.destroyAllWindows()
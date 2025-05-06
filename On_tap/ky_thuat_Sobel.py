import cv2

img = cv2.imread(r'C:\Anhdep\trump.jpg')
#Sử dụng hàm lọc ảnh Gauss để loại bớt nhiễu
new = cv2.GaussianBlur(img, (5,5), 7)
#Chuyển đổi sanh ảnh xám
gray = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)
#Sử dụng hàm Sobel
gra_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, 5)
gra_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, 5)
#Lấy trị tuyệt đối và chuyển đổi kết quả thành 8-bit
abs_gra_x = cv2.convertScaleAbs(gra_x)
abs_gra_y = cv2.convertScaleAbs(gra_y)
#Tính trọng số của 2 mảng (2 ảnh)
grad = cv2.addWeighted(abs_gra_x, 0.5, abs_gra_y, 0.5, 0)
#Hiển thị
cv2.imshow('Anh đẹp', grad)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Anhdep\trump.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
x = int(input('Nhap x: '))
y = int(input('Nhap y: '))
h = int(input('Nhap h: '))
w = int(input('Nhap w: '))
#Cắt ảnh
crop = gray[y:y+h, x:x+w]
#Sử dụng bộ lọc Gauss
gauss = cv2.GaussianBlur(crop, (5,5), 7)
#Phân ngưỡng ảnh bằng bộ lọc thích nghi
th1 = cv2.adaptiveThreshold(gauss, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 0)

#Hiển thị trên matplotlib
plt.subplot(141), plt.imshow(crop, cmap='gray'), plt.axis('off'), plt.title('Anh cat')
plt.subplot(142), plt.imshow(gauss, cmap='gray'), plt.axis('off'), plt.title('Gauss')
plt.subplot(143), plt.imshow(th1, cmap='gray'), plt.axis('off'), plt.title('Threshoding')
plt.subplot(144), plt.imshow(gray, cmap='gray'), plt.axis('off'), plt.title('Anh goc')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import matplotlib.pyplot as plt


img = cv2.imread(r'C:\Anhdep\1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
x = float(input("Nhap x: "))
y = float(input("Nhap y: "))
new = cv2.resize(gray, None, fx=x, fy=y)
#Thay doi anh
thresh = cv2.adaptiveThreshold(new, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#Hien thi
plt.subplot(131), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Anh goc'), plt.axis('off')
plt.subplot(132), plt.imshow(new, cmap='gray'), plt.title('Anh cat'), plt.axis('off')
plt.subplot(133), plt.imshow(thresh, cmap='gray'), plt.title('Anh phan nguong'), plt.axis('off')
plt.show()
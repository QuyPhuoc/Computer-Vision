import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'/home/phuoc/Image/1.jpg')
img_new = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
x = float(input('Nhap x: '))
y = float(input('Nhap y: '))
new = cv2.resize(img, None, fx=x, fy=y)
#Chuyen doi anh xam
gray = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)
#Su dung Gauss
gauss = cv2.GaussianBlur(gray, (5,5), 7)
#Sobel
grad_x = cv2.Sobel(gauss, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(gauss, cv2.CV_64F, 0, 1, ksize=3)
#LẤy trị tuyệt đối
abs_grad_x = cv2.convertScaleAbs(grad_x)
abs_grad_y = cv2.convertScaleAbs(grad_y)
#Tính trong so
grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

plt.subplot(121), plt.imshow(img_new), plt.axis('off'), plt.title('Anh goc')
plt.subplot(122), plt.imshow(grad, cmap='gray'), plt.axis('off'), plt.title('Anh Sobel')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
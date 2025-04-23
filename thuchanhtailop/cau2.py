import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r'C:\Anhdep\trump.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(gray, (5,5), 0)
#Nhập x
x = int(input('Nhap x: '))
#Sử dụng phân ngưỡng nhị phân được nhập vào bàn phím
thresh = cv2.adaptiveThreshold(gauss, x, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,0)
kernel = np.ones((5,5), dtype=np.uint8)
#Phép mở ảnh
open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
#Phép đóng ảnh
close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

#Áp dụng sobel
grad_x = cv2.Sobel(gauss, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(gauss, cv2.CV_64F, 0, 1, ksize=3)
#Lấy trị tuyệt đối
abs_grad_x = cv2.convertScaleAbs(grad_x)
abs_grad_y = cv2.convertScaleAbs(grad_y)
#Tính trọng số của 2 mảng (2 ảnh)
grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
#Hiển thị ảnh
plt.subplot(331), plt.imshow(gray, cmap='gray'), plt.axis('off'), plt.title('gray')
plt.subplot(332), plt.imshow(gauss, cmap='gray'), plt.axis('off'), plt.title('gauss')
plt.subplot(333), plt.imshow(thresh, cmap='gray'), plt.axis('off'), plt.title('thresh')
plt.subplot(334), plt.imshow(open, cmap='gray'), plt.axis('off'), plt.title('open')
plt.subplot(335), plt.imshow(close, cmap='gray'), plt.axis('off'), plt.title('close')
plt.subplot(336), plt.imshow(grad, cmap='gray'), plt.axis('off'), plt.title('grad')
plt.show()

# Nhấn Q để lưu lại kết quả
while True:
        if ord('q'):
            cv2.imwrite(r'C:\CV\Bai thuc hanh 4\Image\xam.jpg', gray)
            cv2.imwrite(r'C:\CV\Bai thuc hanh 4\Image\gauss.jpg', gauss)
            cv2.imwrite(r'C:\CV\Bai thuc hanh 4\Image\thresh.jpg', thresh)
            cv2.imwrite(r'C:\CV\Bai thuc hanh 4\Image\open.jpg', open)
            cv2.imwrite(r'C:\CV\Bai thuc hanh 4\Image\close.jpg', close)
            cv2.imwrite(r'C:\CV\Bai thuc hanh 4\Image\grad.jpg', grad)
            print('OKE, DONE')
            break
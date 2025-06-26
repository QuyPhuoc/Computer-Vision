import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Anhdep\linhquby.jpg')
#a. Doi anh goc sang he mau BGR
img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
#b. Doi anh goc sang anh xam
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Hien thi
plt.subplot(211), plt.imshow(img_bgr), plt.axis('off'), plt.title('BGR')
plt.subplot(212), plt.imshow(img_gray, cmap='gray'), plt.axis('off'), plt.title('GRAY')
plt.show()
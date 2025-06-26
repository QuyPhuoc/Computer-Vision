import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Anhdep\linhquby.jpg')
#a Khu nhieu bang bo loc Gauss
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(img_gray, (5, 5), 7)
#b Phan nguong toi uu
ret, threshotsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
#c Tach bien Canny
canny = cv2.Canny(img_gray, 100, 200)
#d Matplotlib
plt.subplot(441), plt.imshow(cv2.cvtColor(img, cv2.COLOR_RGB2BGR)), plt.axis('off'), plt.title('Anh goc')
plt.subplot(442), plt.imshow(gauss, cmap='gray'), plt.axis('off'), plt.title('gauss')
plt.subplot(443), plt.imshow(threshotsu, cmap='gray'), plt.axis('off'), plt.title('otsu')
plt.subplot(444), plt.imshow(canny, cmap='gray'), plt.axis('off'), plt.title('canny')
plt.show()
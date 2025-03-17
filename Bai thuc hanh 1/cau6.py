import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Anhdep\linhquby.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(gray_img)
plt.axis('off')
plt.show()



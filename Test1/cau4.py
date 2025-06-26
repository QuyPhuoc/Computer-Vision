import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Anhdep\linhquby.jpg')
kernel = np.ones((5,5), np.uint8)
open_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
gray = cv2.cvtColor(open_img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contour,_ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_copy = img.copy()
new = cv2.drawContours(img_copy, contour, -1, (0,0, 255), 2)
#Matplot
plt.subplot(211), plt.imshow(cv2.cvtColor(open_img, cv2.COLOR_BGR2RGB)), plt.axis('off'), plt.title('open')
plt.subplot(212), plt.imshow(cv2.cvtColor(new, cv2.COLOR_BGR2RGB)), plt.axis('off'), plt.title('Contours')
plt.show()

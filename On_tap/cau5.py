import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Anhdep\trump.jpg')
img_new = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
h,w = img.shape[:2]
crop = img[:, 0:w//2]
gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
neg_img = 255 - crop
neg_new = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.subplot(131), plt.imshow(gray, cmap='gray'), plt.axis('off'), plt.title('Xam')
plt.subplot(132), plt.imshow(neg_img, cmap='gray'), plt.axis('off'), plt.title('Anh am ban')
plt.subplot(133), plt.imshow(img_new), plt.axis('off'), plt.title('Anh goc')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'/home/phuoc/Image/1.jpg')
h, w = img.shape[:2]
new = 255 - img
crop = img[0:h, 0:w//2]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.subplot(131), plt.imshow(new, cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)), plt.axis('off'), plt.title('Anh am ban')
plt.subplot(132), plt.imshow(gray), plt.axis('off'), plt.title('Anh xam')
plt.subplot(133), plt.imshow(img, cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.axis('off'), plt.title('Anh goc')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
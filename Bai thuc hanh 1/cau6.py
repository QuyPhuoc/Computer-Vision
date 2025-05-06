import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Anhdep\1.jpg')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

plt.subplot(121), plt.imshow(img1), plt.title('Anh thuong'), plt.axis('off')
plt.subplot(122), plt.imshow(img_gray, cmap='gray'), plt.title('Anh xam'), plt.axis('off')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
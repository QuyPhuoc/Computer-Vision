import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Anhdep\trump.jpg')
img_new = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.subplot(121), plt.imshow(gray, cmap='gray'), plt.axis('off'), plt.title('Anh xam')
plt.subplot(122), plt.imshow(img_new), plt.axis('off'), plt.title('Anh goc')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
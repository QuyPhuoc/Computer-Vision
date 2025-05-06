import cv2
import matplotlib.pyplot as plt


img = cv2.imread(r'C:\Anhdep\trump.jpg')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, threshold_binary = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
adaptive_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 0)
adaptive_gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 0)
ret, thred_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
print(ret)

plt.subplot(161), plt.imshow(img1), plt.title('Anh goc'), plt.axis('off')
plt.subplot(162), plt.imshow(gray, cmap='gray'), plt.title('Anh xam'), plt.axis('off')
plt.subplot(163), plt.imshow(threshold_binary, cmap='gray'), plt.title('thredshold_binary'), plt.axis('off')
plt.subplot(164), plt.imshow(adaptive_mean, cmap='gray'), plt.title('adaptive_mean'), plt.axis('off')
plt.subplot(165), plt.imshow(adaptive_gaussian, cmap='gray'), plt.title('adaptive_gaussian'), plt.axis('off')
plt.subplot(166), plt.imshow(thred_otsu, cmap='gray'), plt.title('thred_otsu'), plt.axis('off')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
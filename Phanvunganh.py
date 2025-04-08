#Phân ngưỡng nhị phân
import cv2
import matplotlib.pyplot as plt
from torch.ao.nn.quantized.functional import threshold

img = cv2.imread(r'C:\Anhdep\trump.jpg')
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, threshold_binary = cv2.threshold(gray, 140,255, cv2.THRESH_BINARY)
adaptive_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 0)
adaptive_gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 0)
ret, thred_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
# cv2.imshow('Anh goc', img)
# cv2.imshow('Anh xam', gray)
cv2.imshow('Mean', adaptive_mean)
cv2.imshow('Adaptive', adaptive_gaussian)
cv2.imshow('anh phan nguong', threshold_binary)
cv2.imshow('OTSU', thred_otsu)
print(ret)
# plt.subplot(131), plt.imshow(img1), plt.axis('off'), plt.title('Anh goc')
# plt.subplot(132), plt.imshow(gray, cmap='gray'), plt.axis('off'), plt.title('Anh xam')
# plt.subplot(133), plt.imshow(threshold_binary), plt.axis('off'), plt.title('Anh nhi phan')
# plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
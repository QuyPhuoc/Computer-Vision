import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Anhdep\coco.jpg')
img = cv2.resize(img, None, fx = 2, fy = 2)

#Sử dụng các bộ lọc khác nhau
#Bộ lọc trung bình
img_blur = cv2.blur(img, (5,5))
#Bộ lọc trung vị
img_median = cv2.medianBlur(img, 7)
#Bộ lọc Gauss
img_gauss = cv2.GaussianBlur(img, (5,5), 9)
#Bộ lọc song phương
img_bilateral = cv2.bilateralFilter(img, 9, 50, 50)

#Chuyển đổi sang hệ màu RGB
new_blur = cv2.cvtColor(img_blur, cv2.COLOR_BGR2RGB)
new_median = cv2.cvtColor(img_median, cv2.COLOR_BGR2RGB)
new_gauss = cv2.cvtColor(img_gauss, cv2.COLOR_BGR2RGB)
new_bilateral = cv2.cvtColor(img_bilateral, cv2.COLOR_BGR2RGB)

#Hiển thị
plt.subplot(231), plt.title('Blur'), plt.axis('off'), plt.imshow(new_blur)
plt.subplot(232), plt.title('Median'), plt.axis('off'), plt.imshow(new_median)
plt.subplot(233), plt.title('Gauss'), plt.axis('off'), plt.imshow(new_gauss)
plt.subplot(234), plt.title('Bilateral'), plt.axis('off'), plt.imshow(new_bilateral)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
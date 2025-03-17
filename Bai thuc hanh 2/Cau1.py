import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Anhdep\1.jpg')
neg_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Anh hoa hong', img)
# cv2.imshow('Anh da muc xam', neg_img)
#Đổi màu vì matplotlib dùng hệ màu RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
neg_img_new = cv2.cvtColor(neg_img, cv2.COLOR_BGR2RGB)
#Sử dụng matplotlib để hiện 2 ảnh
plt.subplot(311), plt.imshow(img_rgb), plt.title('Anh 1'), plt.axis('off')
plt.subplot(312), plt.imshow(neg_img_new), plt.title('Anh 2'), plt.axis('off')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
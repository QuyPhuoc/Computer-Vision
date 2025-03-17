import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Anhdep\1.jpg')
#Cat anh
h,w = img.shape[:2]
crop = img[:, 0:w//2]
#Lấy kích thước ảnh
anh_xam = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
anh_am_ban = 255 - crop
#Đổi ảnh sang hệ màu của matplotlip
img_new = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
crop_new = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
anh_Xam = cv2.cvtColor(anh_xam, cv2.COLOR_BGR2RGB)
anh_Am_ban = cv2.cvtColor(anh_am_ban, cv2.COLOR_BGR2RGB)
#Hiện ảnh
plt.subplot(241), plt.imshow(img_new), plt.title('Anh 1'), plt.axis('off')
plt.subplot(242), plt.imshow(anh_Xam), plt.title('Anh 2'), plt.axis('off')
plt.subplot(243), plt.imshow(anh_Am_ban), plt.title('Anh 3'), plt.axis('off')
plt.subplot(244), plt.imshow(crop_new), plt.title('Anh 4'), plt.axis('off')
plt.show()
cv2.waitKey()
cv2.destroyAllWindows() 
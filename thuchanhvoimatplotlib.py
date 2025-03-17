import matplotlib.pyplot as plt
import cv2
from matplotlib.pyplot import title

#from matplotlib import pyplot as plt
img = cv2.imread(r'C:/Anhdep/hoahong.jpg')
crop = img[10:200, 20:500]
neg_img = 255 - crop
#Trong thư viện opencv, sử dụng hệ màu BGR
#Trong thư viện matplotlib, sử dụng hệ màu RGB
#Vì vậy phải đổi đúng hệ màu
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
crop = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
neg_img = cv2.cvtColor(neg_img, cv2.COLOR_BGR2RGB)
#Hiện ảnh trên matplotlib
array_img = [img_rgb, crop, neg_img]
title_array = ['Anh 1', 'Anh 2', 'Anh 3']
for i in range(3):
    plt.subplot(1, 3, i + 1), plt.imshow(array_img[i]), plt.axis('off'), plt.title(title_array[i])
# plt.subplot(311), plt.imshow(img_rgb), plt.axis('off'), plt.title('Anh 1')
# plt.subplot(312), plt.imshow(crop), plt.axis('off'), plt.title('Anh 2')
# plt.subplot(313), plt.imshow(neg_img), plt.axis('off'), plt.title('Anh 3')
plt.show() #Nếu không có lệnh này, ảnh sẽ không hiện

# cv2.imshow('Anh', img)
# cv2.imshow('Anh am ban', neg_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
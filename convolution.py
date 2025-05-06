import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Anhdep\coco.jpg')
img = cv2.resize(img, None, fx = 2, fy = 2)
cv2.namedWindow('noise_img')

Blur = 1

def get_Blur(pos):
    global Blur
    Blur = pos
    if Blur % 2 == 0:
        Blur += 1
#Tạo trackbar
cv2.createTrackbar('Blur', 'noise_img', Blur, 55, get_Blur)

while True:
    new = cv2.GaussianBlur(img, (Blur,Blur), 5)
    cv2.imshow('noise_img', new)
    if cv2.waitKey(20) == ord('q'):break;

cv2.waitKey(0)
cv2.destroyAllWindows()

#Sử dụng bộ lọc
# img_blur = cv2.blur(img, (9,9))
# res_median = cv2.medianBlur(img, 7)
# res_gauss = cv2.GaussianBlur(img, (5,5), 7)
# res_bilateral = cv2.bilateralFilter(img,  9, 50, 50)

# Chuyển đổi hệ màu
# new = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# new_blur = cv2.cvtColor(img_blur, cv2.COLOR_BGR2RGB)
# new_median = cv2.cvtColor(res_median, cv2.COLOR_BGR2RGB)
# new_gauss = cv2.cvtColor(res_gauss, cv2.COLOR_BGR2RGB)
# new_bilateral = cv2.cvtColor(res_bilateral, cv2.COLOR_BGR2RGB)

#In ảnh
# plt.subplot(231), plt.imshow(img),plt.title('Anh goc'), plt.axis('off')
# plt.subplot(232), plt.imshow(res_median), plt.title('Median'), plt.axis('off')
# plt.subplot(233), plt.imshow(res_gauss),plt.title('Gauss'), plt.axis('off')
# plt.subplot(234), plt.imshow(res_bilateral), plt.title('Bilatetal'),plt.axis('off')
# plt.subplot(235), plt.imshow(img_blur), plt.title('blur'),plt.axis('off')
# plt.subplot(231), plt.imshow(new),plt.title('Anh goc'), plt.axis('off')
# plt.subplot(232), plt.imshow(new_median), plt.title('Median'), plt.axis('off')
# plt.subplot(233), plt.imshow(new_gauss),plt.title('Gauss'), plt.axis('off')
# plt.subplot(234), plt.imshow(new_bilateral), plt.title('Bilatetal'),plt.axis('off')
# plt.subplot(235), plt.imshow(new_bilateral), plt.title('blur'),plt.axis('off')
# plt.show()

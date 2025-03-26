import cv2
from PIL.ImageFilter import GaussianBlur
from sympy.polys.polyoptions import Gaussian

img = cv2.imread(r'C:\Anhdep\coco.jpg')
cv2.namedWindow('Anh dep')
cv2.resize(img, None, fx = 5, fy = 5)

Gaussian = 1

def get_Gauss(pos):
    global Gaussian
    Gaussian = pos
    if Gaussian % 2 == 0:
        Gaussian += 1
#Tạo trackbar
cv2.createTrackbar('Kernel', 'Anh dep', Gaussian, 50, get_Gauss)
while True:
    #Sử dụng Bộ lọc Gauss
    img_gauss = cv2.GaussianBlur(img, (Gaussian, Gaussian), 9)
    cv2.imshow('Anh dep', img_gauss)
    # Lưu ảnh khi nhấn 's'
    if cv2.waitKey(20) == ord('s'):
        cv2.imwrite(r'C:\Anhdep\img_gass.jpg', img_gauss)
    if cv2.waitKey(20) == ord('q'): break

cv2.destroyAllWindows()
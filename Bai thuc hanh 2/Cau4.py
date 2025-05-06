import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Anhdep\1.jpg')
#Thay đổi kích thước
img_new = cv2.resize(img, None, fx = 1.5, fy = 1.5)
cv2.imshow('Anh mới', img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
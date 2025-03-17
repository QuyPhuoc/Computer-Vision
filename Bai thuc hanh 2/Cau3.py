import cv2

img = cv2.imread(r'C:\Anhdep\1.jpg')
x = int(input('Nhap kich thuoc x: '))
y = int(input('Nhap kich thuoc y: '))
img_New = cv2.resize(img, (x, y))
cv2.imshow('Anh moi', img_New)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

img = cv2.imread(r'C:\Anhdep\1.jpg')
print(img.shape)
h,w = img.shape[:2]
b, g, r = img[200, 100] #Trong OpenCV thì toạ độ sẽ là [y,x]
print(f'Giá trị màu tại toạ độ [100,200]: B={b}, G = {g}, R = {r}')

x1 = int(input('Nhap x1: '))
y1 = int(input('Nhap y1: '))
x2 = int(input('Nhap x2: '))
y2 = int(input('Nhap y2: '))

crop_img = img[y1: y2, x1: x2]

cv2.imshow('Anh goc', img)
cv2.imshow('Crop', crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

img = cv2.imread(r'C:\Anhdep\1.jpg')
x = int(input('Nhap toa do x: '))
y = int(input('Nhap toa do y: '))
b, g, r = img[y, x]
print(f'Toa do diem anh la: B = {b}, G = {g}, R = {r}')

cv2.imshow('New', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
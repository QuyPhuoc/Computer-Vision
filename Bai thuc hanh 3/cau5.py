import cv2

img = cv2.imread(r'C:\Anhdep\1.jpg')

x = float(input('Nhap vao kich thuoc x: '))
y = float(input('Nhap vao kich thuoc y: '))

new_img = cv2.resize(img, None, fx = x, fy= y)

cv2.imshow('Anh goc', img)
cv2.imshow('New', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

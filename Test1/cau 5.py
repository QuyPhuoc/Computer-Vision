import cv2

img = cv2.imread(r'C:\Anhdep\linhquby.jpg')
x1 = int(input('Nhap x1: '))
y1 = int(input('Nhap y1: '))
x2 = int(input('Nhap x2: '))
y2 = int(input('Nhap y2: '))

img_crop = img[y1:y2, x1:x2]
print('Kich thuoc anh cat', img_crop.shape[:2])
cv2.imshow('Anh cat', img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
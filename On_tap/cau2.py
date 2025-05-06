import cv2

img = cv2.imread(r'C:\Anhdep\trump.jpg')

x = int(input('Nhap toa do x: '))
y = int(input('Nhap toa do y: '))

b,g,r = img[y, x]
print(f'Giá trị màu tại toạ độ điểm ảnh là: {b}, {g}, {r}')
cv2.imshow('Anh', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
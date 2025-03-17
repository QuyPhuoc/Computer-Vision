import cv2
img = cv2.imread("C:\Anhdep\hoahong.jpg")
cv2.imshow("Hoa hong", img)
cv2.waitKey(1)
x = int(input('Nhap toa do x: '))
y = int(input('Nhap toa do y: '))
if 0 <= x < img.shape[1] and 0 <= y < img.shape[1]:
    (b, g, r) = img[y,x]
    print(f'Gia tri mau tai ({x}, {y}) la: BRG = ({b},{g},{r})')
else:
    print('Gia tri khong hop le')

cv2.waitKey(0)
cv2.destroyAllWindows()




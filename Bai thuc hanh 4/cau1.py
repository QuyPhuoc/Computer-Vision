import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Anhdep\trump.jpg')
new = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
h, w = img.shape[:2]
#Nhập X, nhập Y
x = int(input('Nhap x: '))
y = int(input('Nhap y: '))
crop = img[y:y+h, x:x+w]
gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
ret2,th2 =  cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

plt.subplot(131), plt.imshow(th2, cmap='gray'), plt.axis('off'), plt.title('OTSU')
plt.subplot(132), plt.imshow(gray, cmap='gray'), plt.axis('off'), plt.title('Gray')
plt.subplot(133), plt.imshow(new), plt.axis('off'), plt.title('Anh goc')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
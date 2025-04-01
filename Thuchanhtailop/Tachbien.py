import cv2
import matplotlib.pyplot as plt


img = cv2.imread(r'C:\Anhdep\trump.jpg')
#Sobel
#Chuyển ảnh thành xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Khử nhiễu
gauss = cv2.GaussianBlur(gray, (5,5), 7)
#Áp dụng Sobel
grad_x = cv2.Sobel(gauss, cv2.CV_64F,1, 0, ksize=3)
grad_y = cv2.Sobel(gauss, cv2.CV_64F, 0, 1, ksize=3)
#Lấy giá trị tuyệt đối
abs_grad_x = cv2.convertScaleAbs(grad_x)
abs_grad_y = cv2.convertScaleAbs(grad_y)
#Tính trọng số
sobel = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

#Laplace
laplace = cv2.Laplacian(gauss, cv2.CV_64F, ksize=3)
#Lấy giá trị tuyệt đối cho Laplace
abs_lap = cv2.convertScaleAbs(laplace)
#Canny
canny = cv2.Canny(gauss, 50, 100)

plt.subplot(311), plt.imshow(sobel, cmap='gray'), plt.title('Sobel'), plt.axis('off')
plt.subplot(312), plt.imshow(abs_lap, cmap='gray'), plt.title('Laplace'), plt.axis('off')
plt.subplot(313), plt.imshow(canny, cmap='gray'), plt.title('Canny'), plt.axis('off')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
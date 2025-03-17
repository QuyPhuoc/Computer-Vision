import cv2
img = cv2.imread(r'C:\Anhdep\1.jpg')
#Thu phóng theo tỷ lệ, theo tỉ lệ x, y bao nhiêu
new_img = cv2.resize(img, None, fx = 1.2, fy = 1.2)
#Thu phóng theo kích thước cố định
new_img1 = cv2.resize(img, (500, 500))
cv2.imshow('Anh dep', img)
cv2.imshow('Anh moi', new_img)
cv2.imshow('Anh moi 1', new_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
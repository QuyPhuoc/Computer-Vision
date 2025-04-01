import cv2

img = cv2.imread(r'C:\Anhdep\trump.jpg')
cv2.namedWindow('New')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Khử nhiễu
gauss = cv2.GaussianBlur(gray, (5,5), 7)

X = 0
Y = X * 3
def Demo(pos):
    global X
    X = pos

#Tạo trackbar
cv2.createTrackbar('Canny', 'New', X, Y, Demo)
while True:
    canny = cv2.Canny(gauss, X, Y)
    cv2.imshow('New', canny)
    if cv2.waitKey(20) == ord('q'): break

cv2.destroyAllWindows()
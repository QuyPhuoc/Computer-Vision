import cv2

img = cv2.imread(r'C:\Anhdep\trump.jpg')
cv2.namedWindow('trump')
img_new = cv2.resize(img, None, fx=0.5, fy=0.5)
h,w = img.shape[:2]
x = 0
y = 0
def get_x(pos):
    global x
    x = pos

def get_y(pos):
    global y
    y = pos

cv2.createTrackbar('X', 'trump', x, 100, get_x)
cv2.createTrackbar('Y', 'trump', y, 100, get_y)

while True:
    if ord('p'):
        cv2.imshow('trump', img_new)
    if ord('s'):
        cv2.imwrite(r'/thuchanhtailop/Image/Image.jpg', img)
    if ord('q'): break

cv2.waitKey(0)
cv2.destroyAllWindows()
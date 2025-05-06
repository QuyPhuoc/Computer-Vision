import cv2

img = cv2.imread(r'/home/phuoc/Image/1.jpg')
h,w = img.shape[:2]
cv2.namedWindow('Erosion')
x = 0

def get_X(*args):
    global x
    x = cv2.getTrackbarPos("X","Erosion")

cv2.createTrackbar('X', 'Erosion', 0,360, get_X)

while True:
    M = cv2.getRotationMatrix2D(center=(h//2, w//2), angle=x, scale=1.0)
    img_2 = cv2.warpAffine(img, M, (w,h))
    cv2.imshow('Erosion', img_2)
    if cv2.waitKey(25) == ord('q'):
        break

cv2.destroyAllWindows()
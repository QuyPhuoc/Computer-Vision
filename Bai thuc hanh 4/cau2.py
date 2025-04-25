import cv2

img = cv2.imread(r'C:\Anhdep\trump.jpg')
cv2.namedWindow('trump')
x = 1
def get_x(pos):
    global x
    x = pos

    if x % 2 == 0:
       x += 1
    if x < 1:
       x = 1
cv2.createTrackbar('X', 'trump', 1, 255, get_x)
while True:
    img_median = cv2.medianBlur(img, x)
    cv2.imshow('trump', img_median)
    if cv2.waitKey(25) == ord('s'):
        cv2.imwrite(r'C:\Anhdep\new.jpg', img_median)
    if cv2.waitKey(25) == ord('q'): break

cv2.destroyAllWindows()
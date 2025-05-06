import cv2


img = cv2.imread(r'C:\Anhdep\1.jpg')
cv2.namedWindow('Trackbar')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
x= 0
def get_X(pos):
    global x
    x = pos

#Create trackbar
cv2.createTrackbar('x', 'Trackbar', x, 255, get_X)
while True:
    ret, threshold_binary = cv2.threshold(gray, x, 255, cv2.THRESH_BINARY)
    cv2.imshow('Trackbar', threshold_binary)
    print(ret)
    if cv2.waitKey(25) == ord('q'): break

cv2.waitKey(0)
cv2.destroyAllWindows()
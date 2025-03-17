import cv2
img = cv2.imread(r'C:\Anhdep\1.jpg')
cv2.namedWindow('Hoa hong')
h,w = img.shape[:2]
tX = 0
def get_tX(pos):
    global tX
    tX = pos

# def get_tY(pos):
#     global tY
#     tY = pos

#Tạo trackbar
cv2.createTrackbar('Xoay anh', 'Hoa hong', 0, 360, get_tX)
while True:
    M = cv2.getRotationMatrix2D((w / 2, h / 2), -tX, 0.8)
    img_new = cv2.warpAffine(img, M, (w,h))
    cv2.imshow('Hoa hong', img_new)
    if cv2.waitKey(20) == ord('q'): break
cv2.waitKey(0)
cv2.destroyAllWindows()
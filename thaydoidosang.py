import cv2


img = cv2.imread(r'C:\Anhdep\1.jpg')
print(img.shape)
#Tao ten cua so
cv2.namedWindow('CanhToan')
contrast = 1
brightness = 0
#Tao ham de truyen cho thanh trackbar
def get_contrast(pos):
    global contrast
    contrast = pos / 10 #lay anh nhan voi do tuong phan roi chia cho 10
def get_brightness(pos):
    global brightness
    brightness = pos

#Tao 2 thanh trackbar
cv2.createTrackbar('Contrast: ', 'CanhToan', 0, 30, get_contrast)
cv2.createTrackbar('Brightness: ', 'CanhToan', 10, 100, get_brightness)
#Cho vao vong lap
while True:
    img_new = cv2.convertScaleAbs(img, alpha = brightness, beta = contrast)
    print(contrast, brightness)
    cv2.imshow('CanhToan', img_new)
    if cv2.waitKey(20) == ord('q') : break
cv2.destroyAllWindows()
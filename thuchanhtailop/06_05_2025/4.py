# import cv2
# from numpy.ma.extras import median
#
# img = cv2.imread(r'/home/phuoc/Image/1.jpg')
# cv2.namedWindow('Hoa hong')
#
# x = 0
# def get_X(pos):
#     global x
#     x = pos
#     if x % 2 == 0:
#         x += 1
# cv2.createTrackbar('X', 'Hoa hong', x, 10, get_X)
#
# while True:
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     median_x = cv2.medianBlur(gray, 5)
#     if cv2.waitKey(25) == ord('c'):
#         thred = cv2.threshold(median_x, 127, 255, cv2.THRESH_BINARY)
#         contour = cv2.findContours(median_x, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#         copies = median_x.copy()
#         cv2.imwrite('r/home/phuoc/Image/new.jpg', contour)
#     if cv2.waitKey(25) == ord('q'):
#         break
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
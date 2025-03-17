import cv2

img = cv2.imread(r'C:\Anhdep\hoahong.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Anh xam', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()





# x, y = img.shape[:2]
# img1 = np.empty((x, y), dtype=np.uint8)
# img2 = np.zeros((x, y), dtype=np.uint8)
# threshould = 128
#
# for i in range(x):
#     for j in range(y):
#         img1[i, j] = 0.299 * img[i, j, 2] + 0.587 * img[i, j, 1] + 0.114 * img[i, j, 0]
#         if img1[i, j] < threshould:
#             img2[i, j] = 0
#         else:
#             img2[i, j] = 255
#
# #cv2.imshow("test 1: ", img)
# cv2.imshow("test 2: ", img1)
# #cv2.imshow("test 3: ", img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

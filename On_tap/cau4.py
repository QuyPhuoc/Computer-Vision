import cv2

video = cv2.VideoCapture(r'C:\Video\nau an.mp4')
while True:
    ret, frame = video.read()
    if not ret:
        print ('Lỗi đọc frame')
        break
    cv2.imshow('Video', frame)

    if cv2.waitKey(25) == ord('s'):
        cv2.imwrite(r'C:\CV\On_tap\img.jpg', frame)
    if cv2.waitKey(25) == ord('q'): break

cv2.destroyAllWindows()
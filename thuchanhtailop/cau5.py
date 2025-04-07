import cv2

video = cv2.VideoCapture(r'C:\Video\Nau an.mp4')

fps = video.get(5)
print('Số hình trong 1 giây: ', fps)
frame = video.get(7)
print('Tổng số khung: ', frame)

while video.isOpened():
    ret, frame = video.read()
    if ret == True:
        video_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Video xam', video_gray)
    if cv2.waitKey(25) == ord('s'):
        cv2.imwrite(r'C:\Anhdep\Xam.jpg', frame)
    if cv2.waitKey(25) == ord('q'): break

video.release()
cv2.destroyAllWindows()
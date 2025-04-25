import cv2

video = cv2.VideoCapture(r'C:\Video\Nau an.mp4')
if video.isOpened() == False:
    print("Error")
else:
    fps = video.get(5)
    print('Số khung hình trên giây: ', fps)
    frame_count = video.get(7)
    print('Số khung hình: ', frame_count)

while True:
    ret, frame = video.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(25) == ord('s'):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(r'C:\Video\new.jpg', gray)
    if cv2.waitKey(25) == ord('q'): break

cv2.destroyAllWindows()
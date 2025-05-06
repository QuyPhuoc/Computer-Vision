import cv2

video = cv2.VideoCapture(r'C:\Video\Nau an.mp4')
while True:
    ret, frame = video.read()
    if ret:
       cv2.imshow('Vide0 nau an', frame)
    if cv2.waitKey(25) == ord('s'):
        cv2.imwrite(r'C:\Anhdep\Nau an.jpg', frame)
    if cv2.waitKey(25) == ord('q'): break

video.release()
cv2.destroyAllWindows()
import cv2
import os

filename = ('Anhdep/trump.jpg')


def detect(filename):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Đọc hình ảnh
    img = cv2.imread(filename)

    # Kiểm tra xem hình ảnh có tồn tại không
    if img is None:
        print("Không thể đọc hình ảnh:", filename)
        return

    # Chuyển đổi hình ảnh sang màu xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Phát hiện khuôn mặt
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Vẽ hình chữ nhật quanh khuôn mặt
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Hiển thị hình ảnh
    cv2.namedWindow('Donal Trump')
    cv2.imshow('Donal Trump', img)

    # Lưu hình ảnh đã xử lý
    cv2.imwrite('./dn.jpg', img)

    # Chờ nhấn phím để đóng cửa sổ
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Gọi hàm để phát hiện khuôn mặt
detect(filename)
import cv2

# Khởi tạo đối tượng VideoCapture để đọc video từ webcam
vid = cv2.VideoCapture(0)

def detect(vid):
    face_cascade_path = 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    while True:
        # Đọc một khung hình từ video
        ret, frame = vid.read()

        if not ret:
            print("Không thể đọc khung hình từ video.")
            break

        # Chuyển đổi khung hình sang màu xám
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Phát hiện khuôn mặt
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        print(f"Đã phát hiện {len(faces)} khuôn mặt.")

        # Vẽ hình chữ nhật quanh các khuôn mặt phát hiện
        for (x, y, w, h) in faces:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Hiển thị khung hình với khuôn mặt đã phát hiện
        cv2.imshow('Phát hiện khuôn mặt', frame)

        # Thoát khi nhấn phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Giải phóng đối tượng VideoCapture và đóng tất cả các cửa sổ
    vid.release()
    cv2.destroyAllWindows()

# Gọi hàm detect với video từ webcam
detect(vid)
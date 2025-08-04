import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera frame not read.")
        continue

    print("Frame dtype:", frame.dtype)
    print("Frame shape:", frame.shape)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print("Gray dtype:", gray.dtype)

    cv2.imshow("Gray", gray)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

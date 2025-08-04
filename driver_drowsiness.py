import cv2

# Constants
EAR_THRESHOLD = 0.25
EAR_CONSEC_FRAMES = 15

counter = 0
status_text = "NO FACE"

# Haar cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam not found")
    exit()

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    if len(faces) == 0:
        status_text = "NO FACE"
        counter = 0  # reset counter if face is gone
    else:
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            ear_values = []

            if len(eyes) == 0:
                # Assume closed eyes (drowsiness)
                counter += 1
                if counter >= EAR_CONSEC_FRAMES:
                    status_text = "DROWSY"
                else:
                    status_text = "SLEEPY"
            else:
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 1)
                    ear = eh / float(ew)
                    ear_values.append(ear)

                if len(ear_values) >= 2:
                    avg_ear = sum(ear_values) / len(ear_values)
                    cv2.putText(frame, f"EAR: {avg_ear:.2f}", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

                    if avg_ear < EAR_THRESHOLD:
                        counter += 1
                        if counter >= EAR_CONSEC_FRAMES:
                            status_text = "DROWSY"
                        else:
                            status_text = "SLEEPY"
                    else:
                        counter = 0
                        status_text = "AWAKE"
                else:
                    # If only one eye detected, don't use EAR — just skip
                    status_text = "SLEEPY"

    # Show status
    cv2.putText(frame, f"STATUS: {status_text}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("Drowsiness Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
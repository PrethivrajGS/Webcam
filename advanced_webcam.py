import cv2

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("""
Press the following keys:
    [n] - Normal Mode
    [g] - Grayscale Mode
    [e] - Edge Detection Mode
    [f] - Face Detection Mode
    [q] - Quit
""")

mode = 'n'  # default mode

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    if mode == 'g':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    elif mode == 'e':
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.Canny(gray, 50, 150)

    elif mode == 'f':
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f"Faces: {len(faces)}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # Show the frame
    cv2.imshow("Advanced Webcam", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key in [ord('n'), ord('g'), ord('e'), ord('f')]:
        mode = chr(key)

cap.release()
cv2.destroyAllWindows()

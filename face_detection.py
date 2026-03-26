import cv2

#LOAD HAAR CASCADE 
cascade_path = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

if face_cascade.empty():
    print("Error: Haar cascade file not loaded")
    exit()

#CAMERA SETUP 
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error: Camera not opened")
    exit()

print("Face detection started. Press 'q' to quit")

# MAIN LOOP 
while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to grab frame")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Face detection
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(60, 60)
    )

    # Count faces
    face_count = len(faces)

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display face count
    cv2.putText(
        frame,
        f'Faces: {face_count}',
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    # Show output
    cv2.imshow("Face Detection", frame)

    # Exit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#cleanup
cap.release()
cv2.destroyAllWindows()

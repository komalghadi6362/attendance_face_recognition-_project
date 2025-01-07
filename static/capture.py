import cv2
import os

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Initialize webcam
camera = cv2.VideoCapture(0)


def capture_faces(student_id):
    student_folder = f"dataset/{student_id}"
    if not os.path.exists(student_folder):
        os.makedirs(student_folder)

    i = 0
    while i < 20:
        input("Press Enter to capture")
        ret, frame = camera.read()
        if not ret:
            print("Error: Failed to capture frame")
            break

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        if len(faces) == 0:
            print("No face detected. Please try again.")
            continue

        # Save only the first detected face
        x, y, w, h = faces[0]
        face_roi = frame[y : y + h, x : x + w]

        cv2.imwrite(os.path.join(student_folder, f"{i+1}.png"), face_roi)
        print(f"Face {i+1} captured for student {student_id}")
        i += 1


# Input student ID
student_id = input("Enter student ID: ")
capture_faces(student_id)

# Release webcam
camera.release()

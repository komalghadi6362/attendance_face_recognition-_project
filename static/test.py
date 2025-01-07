import cv2
import os

# Load the trained LBPH face recognizer model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_recognizer_model.yml")  # Load the trained model

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Initialize the webcam
camera = cv2.VideoCapture(0)

# Create a mapping between student IDs and their corresponding folder names
student_id_mapping = {
    1: "Suraj",
    2: "Karthik",
}

while True:
    # Capture a frame from the webcam
    ret, frame = camera.read()
    if not ret:
        print("Error: Failed to capture frame")
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Iterate through detected faces
    for x, y, w, h in faces:
        # Draw a rectangle around the face region
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Crop the face region for recognition
        face_roi = gray[y : y + h, x : x + w]

        # Perform face recognition
        label, confidence = recognizer.predict(face_roi)

        # Map the numeric label to the corresponding student ID (folder name)
        # print(label)
        student_id = student_id_mapping.get(label, "Unknown")

        # Display the recognized student ID and confidence level
        # text = f"Student ID: {student_id}, Confidence: {confidence:.2f}"
        text = f"Student: {student_id}"
        cv2.putText(
            frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2
        )

    # Display the frame with face detection and recognition
    cv2.imshow("Face Recognition", frame)

    # Wait for 'q' key to quit the program
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()

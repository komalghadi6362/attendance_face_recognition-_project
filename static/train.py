import cv2
import os
import numpy as np

# Define the path to the image folder containing labeled images
image_folder = "dataset"

# Initialize LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()


# Function to load labeled images from the folder
def load_images_from_folder(folder):
    images = []
    labels = []
    student_id_mapping = {}  # Mapping between alphanumeric student IDs and numeric IDs
    current_id = 0

    for subfolder in os.listdir(folder):  # Iterate through subfolders
        subfolder_path = os.path.join(folder, subfolder)
        if os.path.isdir(subfolder_path):  # Check if it's a directory
            current_id += 1
            student_id_mapping[subfolder] = (
                current_id  # Assign a unique numeric ID for each student
            )
            for filename in os.listdir(subfolder_path):
                path = os.path.join(subfolder_path, filename)
                img = cv2.imread(path)
                if img is not None:
                    label = current_id  # Use the numeric ID as the label
                    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    images.append(gray_img)
                    labels.append(int(label))  # Convert label to integer
    return images, labels


# Load labeled images and labels
images, labels = load_images_from_folder(image_folder)

# Train the recognizer
recognizer.train(images, np.array(labels))

# Save the trained model
recognizer.save("face_recognizer_model.yml")

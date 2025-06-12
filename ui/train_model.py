import os
import face_recognition
import pickle
import numpy as np

face_encodings = {}
dataset_path = r"C:\Users\91752\Desktop\Facial_Recognition_Attendance\ui\dataset"

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)
    encodings = []
    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)
        img = face_recognition.load_image_file(img_path)
        encoding = face_recognition.face_encodings(img)
        if encoding:
            encodings.append(encoding[0])
    if encodings:
        face_encodings[person] = np.mean(encodings, axis=0)

with open("trained_model/face_encodings.pkl", "wb") as f:
    pickle.dump(face_encodings, f)

print("Model training complete!")

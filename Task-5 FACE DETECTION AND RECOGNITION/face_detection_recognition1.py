import cv2  
import face_recognition  
import numpy as np  
from PIL import Image  

# Function to locate faces  
def detect_faces(image):  
    face_locations = face_recognition.face_locations(image)  
    return face_locations  

# Function to display detected faces  
def display_faces(image, face_locations):  
    for (top, right, bottom, left) in face_locations:  
        cv2.rectangle(image, (left, top), (right, bottom), (255, 0, 0), 2)  
    return image  

# Load a known image for recognition  
def load_known_face(known_image_path, name):  
    img = face_recognition.load_image_file(known_image_path)  
    img_encoding = face_recognition.face_encodings(img)[0]  
    return (img_encoding, name)  

# Main function for face detection and recognition  
def recognize_faces(video_source=0):  
    # Start video capture  
    video_capture = cv2.VideoCapture(video_source)  

    # Load known faces  
    known_faces = [  
        load_known_face("known_face.jpg", "Known Person")  # Change this path and name to your known face  
        # Add more known faces as needed  
    ]  
    
    known_face_encodings = [face[0] for face in known_faces]  
    known_face_names = [face[1] for face in known_faces]  
    
    while True:  
        # Capture frame-by-frame  
        ret, frame = video_capture.read()  
        
        # Convert frame from BGR to RGB  
        rgb_frame = frame[:, :, ::-1]  

        # Find all face locations and encodings in the current frame  
        face_locations = detect_faces(rgb_frame)  
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)  

        # Loop through each face found, and check if they match any known faces  
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):  
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)  
            name = "Unknown"  

            # Use the known face with the closest encoding  
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)  
            best_match_index = np.argmin(face_distances)  
            if matches[best_match_index]:  
                name = known_face_names[best_match_index]  

            # Draw a box around the face  
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)  
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)  

        # Display the resulting frame  
        cv2.imshow('Video', frame)  

        # Break the loop when 'q' is pressed  
        if cv2.waitKey(1) & 0xFF == ord('q'):  
            break  

    # Release the capture and close windows  
    video_capture.release()  
    cv2.destroyAllWindows()  

# Call the function to start face recognition  
recognize_faces()  # Use 0 for webcam or you can specify a video file path
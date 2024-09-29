import cv2
import os

harcascade = r"D:/git/codesoft-AI/Task-5 FACE DETECTION AND RECOGNITION/haarcascade_frontalface_default.xml"

if not os.path.exists(harcascade):
    print("Error: The file 'haarcascade_frontalface_default.xml' does not exist.")
    exit()

facecascade = cv2.CascadeClassifier(harcascade)

if not facecascade:
    print("Error: Unable to load the cascade classifier.")
    exit()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to open the video capture.")
    exit()

cap.set(3, 640)  
cap.set(4, 480) 

while True:
    success, img = cap.read()

    if not success:
        print("Error: Unable to read the video frame.")
        break

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = facecascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Face", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
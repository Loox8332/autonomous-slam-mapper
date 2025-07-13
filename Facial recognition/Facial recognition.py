import cv2

# Import the Haar Cascade classifier for face detection https://github.com/opencv/opencv/tree/master/data/haarcascades
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") 

video = cv2.VideoCapture(0)
if not video.isOpened():
    raise Exception("Could not open video device")

def detect_faces(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    return frame

while True:
    ret, frame = video.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    faces = detect_faces(frame)

    cv2.imshow("Face Detection", faces)

    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
video.release()
cv2.destroyAllWindows()
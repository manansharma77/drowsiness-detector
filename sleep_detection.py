###
import cv2
import os
import turtle

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

screen = turtle.Screen()
screen.title('User Details')
screen.setup(width=1200, height=700)
screen.bgcolor("lightblue")

name = screen.textinput('User Info', 'Enter your name:')
reg_no = screen.textinput('User Info', 'Enter your registration number:')

screen.bye()

cap = cv2.VideoCapture(0)


eye_closed_frames = 0


FRAME_THRESHOLD = 20

print("Press ESC to exit")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame. Camera issue?")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    eyes_detected = False

    for (x, y, w, h) in faces:
       
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

     
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

        if len(eyes) > 0:
            eyes_detected = True

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

   
    if not eyes_detected:
        eye_closed_frames += 1
    else:
        eye_closed_frames = 0

   
    if eye_closed_frames > FRAME_THRESHOLD:
        cv2.putText(frame, "SLEEPING ALERT!", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        os.system('say "Wake up"')
        os.system('afplay /System/Library/Sounds/Glass.aiff &')  
        print("/a")
    else:
        cv2.putText(frame, "Awake", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(frame, f"Name: {name}", (10, frame.shape[0] - 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, f"Reg: {reg_no}", (10, frame.shape[0] - 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Sleep Detection System", frame)

   
    if cv2.waitKey(1) == 27:
        break


cap.release()
cv2.destroyAllWindows()

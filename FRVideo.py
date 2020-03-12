# -*- coding: utf-8 -*-
"""
@author: karthik
"""

import cv2

#cascPath = "haarcascade_frontalface_default.xml";
cascPath = "haarcascade_frontalface_alt2.xml";
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        #minSize=(30, 30),
        #flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Wait for Esc key to stop 
    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

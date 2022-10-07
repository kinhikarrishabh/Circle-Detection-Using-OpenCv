import cv2 as cv
import mediapipe as mp

VideoCapture=cv.VideoCapture(0)
while True:
  ret,frame=VideoCapture.read()
  if not ret: break

  cv.imshow("Frame",frame)

  if cv.waitKey(1) & 0xFF == (ord("q")): break

VideoCapture.release()
cv.destroyAllWindows()


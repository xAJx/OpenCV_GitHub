import mediapipe as mp
import cv2
face_det = mp.solutions.face_detection
mp_drawing  = mp.solutions.drawing_utils

img = cv2.imread("multi_people.JPG")
newimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
faceDetction = face_det.FaceDetection(model_selection=1)
result = faceDetction.process(newimg)
if not result.detections:
    print("no detect")
else:
    for result in result.detections:
        mp_drawing.draw_detection(img,result)
    cv2.imshow("result",img)
    cv2.waitKey(0)
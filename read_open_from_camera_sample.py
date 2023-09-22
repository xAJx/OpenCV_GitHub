import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX') #mp4v
out = cv2.VideoWriter("output.mp4",fourcc,20.0,(640,480))
while cv2.waitKey(1)!=27:
    ret,frame = cap.read()
    cv2.imshow("frame",frame)
    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()

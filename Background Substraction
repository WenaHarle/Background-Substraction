import cv2
import numpy as np

cap = cv2.VideoCapture("fix.mp4")
_, frame1 = cap.read()
abupertama = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
abupertama = cv2.GaussianBlur(abupertama, (5, 5), 0)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = cap.get(cv2.CAP_PROP_FPS)
result = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('P','I','M','1'), fps, (width, height), isColor=False)

while True:
    _, frame = cap.read()
    frameabu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameabu = cv2.GaussianBlur(frameabu, (5, 5), 0)
    difference = cv2.absdiff(abupertama, frameabu)
    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
    cv2.imshow("frame pertama", frame1)
    cv2.imshow("mentahan", frame)
    cv2.imshow("perbedaaan", difference)
    result.write(difference)
    key = cv2.waitKey(30)
    if key == 27:
        break


result.release()
cap.release()

cv2.destroyAllWindows()

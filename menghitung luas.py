import cv2
import numpy as np

cap = cv2.VideoCapture("fix.mp4")
bac = cv2.VideoCapture("bac2.jpg")
_, frame1 = bac.read()
abupertama = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
abupertama = cv2.GaussianBlur(abupertama, (5, 5), 0)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = cap.get(cv2.CAP_PROP_FPS)
result = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('P','I','M','1'), fps, (width, height), isColor=False)

while True:
    _, frame = cap.read()
    roi = frame[60: 540, 1: 352]
    frameabu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameabu = cv2.GaussianBlur(frameabu, (5, 5), 0)
    difference = cv2.absdiff(abupertama, frameabu)
    _, difference = cv2.threshold(difference, 25, 25, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(difference, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []

    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 6000:
            #cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            detections.append([x, y, w, h])
            cv2.putText(frame, str(w*h), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    print(detections)
    cv2.imshow("roi", roi)
    cv2.imshow("ini", frame)
    cv2.imshow("hasil", difference)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.releasa()
cv2.destroyALLWindows()

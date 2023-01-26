import math

import cv2
import numpy as np

cap = cv2.VideoCapture("fix.mp4")
bac = cv2.VideoCapture("bac2.jpg")
_, frame1 = bac.read()
roi2 = frame1[40: 540, 60: 280]
abupertama = cv2.cvtColor(roi2, cv2.COLOR_BGR2GRAY)
abupertama = cv2.GaussianBlur(abupertama, (5, 5), 0)


count = 0
midold = []

trackob = {}
track_id = 0
while True:
    _, frame = cap.read()
    count += 1

    roi = frame[40: 540, 60: 280]
    frameabu = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    frameabu = cv2.GaussianBlur(frameabu, (5, 5), 0)
    difference = cv2.absdiff(abupertama, frameabu)
    _, difference = cv2.threshold(difference, 25, 225, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(difference, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    detections = []
    #menunjukkan fram sekarang
    midnow = []

    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 6000 and area <11000 :
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 0, 225), 3)

            detections.append([x, y, w, h])
            cv2.putText(roi, str(w*h), (x, y+h), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            cx = int((x + x + w) / 2)
            cy = int((y + y + h) / 2)
            midnow.append((cx, cy))


    if count <= 2:
        for pt in midnow:
            for pt2 in midold:
                distance = math.hypot(pt2[0]-pt[0],pt2[1]-pt[1])

                if distance < 50:
                    trackob[track_id] = pt
                    track_id += 1
    else:

        trackob_copy = trackob.copy()
        midnow_copy = midnow.copy()

        for object_id, pt2 in trackob_copy.items():
            object_exists = False
            for pt in midnow_copy:
                distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])

                #update object position
                if distance < 50:
                    trackob[object_id] = pt
                    object_exists = True
                    if pt in midnow:
                        midnow.remove(pt)
                        continue

                #remove id
            if not object_exists:
                trackob.pop(object_id)

        for pt in midnow:
            trackob[track_id] = pt
            track_id += 1

    for object_id, pt in trackob.items():
        cv2.circle(roi, (x, y), 5, (0, 0, 225), -1)
        cv2.putText(roi, str(object_id), (pt[0], pt[1]+7), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)


    print("tracking obeject")
    print(trackob)
    print("cordinat box")
    print(detections)
    print("cordinat midnow")
    print(midnow)
    print("cordinat midold")
    print(midold)

    midold = midnow.copy()

    cv2.imshow("roi", roi)
    cv2.imshow("ini", frame)
    cv2.imshow("hasil", difference)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.releasa()
cv2.destroyALLWindows()

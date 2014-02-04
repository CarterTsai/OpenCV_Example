#!/usr/bin/env python

# https://dl.dropboxusercontent.com/u/28096936/tuts/motionTrackingTut/finalCode/motionTracking.cpp
import cv2
import sys

sensitivity_value = 20
count = 0
theObject = [0,0]

def searchMovement(thresholdImage, frame):
    objectDetected = 0
    largestContourVec = []
    objectBoundingRectangle = []
    x , y = 0 , 0

    gray =  cv2.cvtColor(thresholdImage, cv2.COLOR_BGR2GRAY)

    contours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours)>0 :
        objectDetected = 1
    else:
        objectDetected = 0
    if objectDetected:
        largestContourVec.append(contours[len(contours) -1])
        bx,by,bw,bh = cv2.boundingRect(largestContourVec[0])
        px  = bx + bw/2
        py  = by + bw/2
        theObject[0] = px
        theObject[0] = py

    x = theObject[0]
    y = theObject[1]
    cv2.circle(frame, (x,y), 20 ,(0,255,0), 2)
    return frame


if __name__ == '__main__':

    if len(sys.argv) == 1:
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(sys.argv[1])
        if not cap.isOpened():
            cap = cv2.VideoCapture(int(sys.argv[1]))

    if not cap.isOpened():
        print 'Cannot initialize vide capture'
        sys.exit(-1)

    while(1):
        count += 1
        ret, frame1 = cap.read()
        if not ret:
            break;

        ret, frame2 = cap.read()
        if not ret:
            break;

        gray = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
        codes, corners, dmtx = cv2.findDataMatrix(gray)
        cv2.drawDataMatrixCodes(frame1, codes, corners)

        cv2.imshow('ShowFrame', frame1)
        absFrame = cv2.absdiff(frame1, frame2)

        cv2.imshow('absFrame', absFrame)
        ret, thresholdFrame = cv2.threshold(absFrame, sensitivity_value
                                       ,255, cv2.THRESH_BINARY)

        for i in xrange(1,6,2):
            thresholdFrame =  cv2.blur(thresholdFrame,(i,i))

        ret, thresholdFrame = cv2.threshold(absFrame, sensitivity_value
                                       ,255, cv2.THRESH_BINARY)


        gy = searchMovement(thresholdFrame,frame1)
        cv2.imshow('thresholdFrame', gy)

        key = cv2.waitKey(30)
        c = chr(key & 255)
        if c in ['q', 'Q', chr(27)]:
            break


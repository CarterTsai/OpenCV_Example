#!/usr/bin/env python

import cv2
import sys

sensitivity_value = 20

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
        cv2.imshow('thresholdFrame', thresholdFrame)

        key = cv2.waitKey(30)
        c = chr(key & 255)
        if c in ['q', 'Q', chr(27)]:
            break


# -*- coding: utf-8 -*-
"""
@author: karthik
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture Frame by Frame
    ret, frame = cap.read()
    
    #Display the resulting frame
    cv2.imshow('recording', frame)
    
    
    k = cv2.waitKey(5) & 0xFF
    if(k == 27):
        break
    
    
cap.release()
cv2.destroyAllWindows()



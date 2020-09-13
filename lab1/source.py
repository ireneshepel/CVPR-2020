import numpy as np
import cv2

cap = cv2.VideoCapture(0)


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

while(cap.isOpened()):

        ret, frame = cap.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        #line
        cv2.line(bgr, (60,20), (100, 100), (0,0,255), 5)
        #rectangle
        cv2.rectangle(bgr, (400,200), (600,150), (0,255,0), 10)
        # write the frame
        out.write(bgr)

        cv2.imshow('frame', bgr)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
out.release()
cv2.destroyAllWindows()

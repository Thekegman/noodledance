import cv2
import numpy as np
from collections import deque
cap = cv2.VideoCapture('spin.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
segment_count = 70
segment_height = int(height/segment_count)
setup_complete =False
frames = []
while(cap.isOpened()):
    ret, new_frame = cap.read()
    if new_frame is None:
        break
    
    frames.append(new_frame)
    
    if len(frames) >= segment_count:    
        segments = []
        for i,frame in enumerate(frames):
            segments.append(frame[i*segment_height:(i+1)*segment_height])
        
        noodled_frame = np.concatenate(segments, axis=0)

        frames.pop(0)

        
        cv2.imshow('frame', noodled_frame)    
        if cv2.waitKey(int(30)) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

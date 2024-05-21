import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dimension=(width,height)
f=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter("video_recorder.mp4",f,30.0,dimension)
start_time=time.time()
dur = 50+4
end_time=start_time+dur
while True:
    image=pyautogui.screenshot()
    frame_1=np.array(image)
    frame=cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)
    output.write(frame) 
    c_time=time.time()
    if c_time>end_time:
        break
output.release()
print(" END ")

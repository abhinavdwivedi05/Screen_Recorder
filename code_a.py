import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time
import sys

width=GetSystemMetrics(0)
height=GetSystemMetrics(1)
dimension=(width,height)
'''setting the dimension for the video'''
f= cv2.VideoWriter_fourcc(*"XVID")
'''setting format for the video'''
vid_name=input("Enter the name for the video: ")
output= cv2.VideoWriter(vid_name,f,30.0,dimension)
while True:
    try:
        dur = int(input("Enter The duration for screen recording in seconds:"))
        if dur<0:
            print("Duration can not be in negative!")
        else:
            break
    except ValueError:
        print("please enter the correct value")

now_start_time= time.time()
end_time= now_start_time+dur
'''setting time for the video'''
print("****Recording Started****")
while True:
    image = pyautogui.screenshot()
    '''getting screenshots'''
    frame_1=np.array(image)
    '''arranging screenshot into an array'''
    frame=cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)
    '''COLOR_BGR2RGB Saves the true color for the screenshots'''

    output.write(frame)
    c_time=time.time() 

    if c_time > end_time:
        break
    '''breaking the loop when endtime is equal to duration + start time'''
output.release()
'''releasing our video'''
print("---Video has been stored in same directory as the code---")


import cv2 
import datetime 
import os

count = 0

in_path = '/home/kj/litmus/mytools/videos/'
files = os.listdir(in_path)
out_path = '/home/kj/litmus/mytools/imgs2/'


def cleanupDir(folder):
    files = os.listdir(folder)
    for f in files:
        os.remove(folder + f)


cleanupDir(out_path)

for file in files:
    if file[-3:] != 'mp4': 
        continue 
    cap = cv2.VideoCapture(in_path + file) 
    if not cap.isOpened(): 
        exit(0) 
    frameFrequency = 30 
    if file[:3] == 't3':
        frameFrequency = 60
    totalFrame = 0 
    while True: 
        ret, frame = cap.read() 
        if ret is False: 
            break 
        count += 1
        totalFrame += 1 
        if totalFrame % frameFrequency == 0:  
            img_name = out_path + str(count) + '.jpg' 
            cv2.imwrite(img_name, frame) 
            print(img_name) 

    cap.release() 
    print('done') 
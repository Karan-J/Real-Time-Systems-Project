import os 
import cv2
import numpy as np


in_path = './imgs1'
files= os.listdir(in_path) 
print(files) 

for file in files: 

    if file[-3:] != 'jpg': 
        continue 

    # print(file[:-4]) 
    f = file[:-4] 

    file_in = "./imgs1/" + file 
    file_out = "./blur/b" + file 

    image = cv2.imread(file_in)
    result = cv2.GaussianBlur(image, (7, 7), 0)

    # (rows, cols) = image.shape[:2]
    # M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)    
    # result = cv2.warpAffine(image, M, (cols, rows))


    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(file_out,result)



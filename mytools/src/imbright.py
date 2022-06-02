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
    file_out = "./bright/br" + file 

    image = cv2.imread(file_in)
    result = image + (80,80,80)

    cv2.imwrite(file_out,result)



import os 
import cv2
import numpy as np


in_path = './imgs1'
files= os.listdir(in_path) 
print(files) 


def sepia(src_image):
    gray = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
    normalized_gray = np.array(gray, np.float32)/255
    #solid color
    sepia = np.ones(src_image.shape)
    sepia[:,:,0] *= 153 #B
    sepia[:,:,1] *= 204 #G
    sepia[:,:,2] *= 255 #R
    #hadamard
    sepia[:,:,0] *= normalized_gray #B
    sepia[:,:,1] *= normalized_gray #G
    sepia[:,:,2] *= normalized_gray #R
    return np.array(sepia, np.uint8)


for file in files: 

    if file[-3:] != 'jpg': 
        continue 

    # print(file[:-4]) 
    f = file[:-4] 

    file_in = "./imgs1/" + file 
    file_out = "./sepia/s" + file 

    image = cv2.imread(file_in)

    result = sepia(image) 
    cv2.imwrite(file_out,result)


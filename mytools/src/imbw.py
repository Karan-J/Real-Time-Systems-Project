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
    file_out = "./baw/bw" + file 

    image = cv2.imread(file_in, cv2.IMREAD_GRAYSCALE)
    thresh = 128
    result = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]

    cv2.imwrite(file_out,result)



# # threshold the image
# img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

# #save image
# cv2.imwrite('D:/black-and-white.png',img_binary)
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
    file_out = "./rotate/r" + file 

    image = cv2.imread(file_in)

    (rows, cols) = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)    
    result = cv2.warpAffine(image, M, (cols, rows))


    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(file_out,result)


# FILE_NAME = 'volleyball.jpg'
# try:
# 	# Read image from the disk.
# 	img = cv2.imread(FILE_NAME)

# 	# Shape of image in terms of pixels.
# 	(rows, cols) = img.shape[:2]

# 	# getRotationMatrix2D creates a matrix needed for transformation.
# 	# We want matrix for rotation w.r.t center to 45 degree without scaling.
# 	M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
# 	res = cv2.warpAffine(img, M, (cols, rows))

# 	# Write image back to disk.
# 	cv2.imwrite('result.jpg', res)
# except IOError:
# 	print ('Error while reading files !!!')

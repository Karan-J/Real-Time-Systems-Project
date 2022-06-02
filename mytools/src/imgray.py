

import cv2 
import os 

# import sys 
# # get output img format 
# outImgType = '.'+sys.argv[1] 

 
# out_path = 'bmps' 
# #get dir's all file's filename 

in_path = './imgs1'
files= os.listdir(in_path) 
print(files) 


# image = cv2.imread('./imgs1/1.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
# cv2.imshow('Original image',image)
# cv2.imshow('Gray image', gray)
  
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# for filename in files:  
#     name = filename.split('.') 
#     if not os.path.isdir(filename):   
#         inImg =os.path.join(in_path,filename) 
#         img = cv2.imread(inImg) 
#         outImg = os.path.join(out_path,name[0]+outImgType) 
#         # sprint(inImg,outImg,cv2.imwrite(outImg,img)) 

# from PIL import Image 

for file in files: 

    if file[-3:] != 'jpg': 
        continue 

    # print(file[:-4]) 
    f = file[:-4] 

    file_in = "./imgs1/" + file 
    file_out = "./gs/g" + file 

    image = cv2.imread(file_in)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(file_out,gray)

    # img = Image.open(file_in) 

    # img.save(file_out) 
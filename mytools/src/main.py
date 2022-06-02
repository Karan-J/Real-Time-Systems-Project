import argparse
import os
import cv2 
import numpy as np
import time 


def cleanupDir(folder):
    files = os.listdir(folder)
    for f in files:
        os.remove(folder + f)


def sepiaHelper(src_image):
    gray = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
    normalized_gray = np.array(gray, np.float32)/255
    #solid color
    sepia = np.ones(src_image.shape)
    sepia[:,:,0] *= 153 #B
    sepia[:,:,1] *= 204 #G
    sepia[:,:,2] *= 255 #R
    sepia[:,:,0] *= normalized_gray #B
    sepia[:,:,1] *= normalized_gray #G
    sepia[:,:,2] *= normalized_gray #R
    return np.array(sepia, np.uint8)


def darken(input_folder, files):
    print('Darkening all the images from : ' + input_folder)

    output_folder = './darkened/'
    prefix = 'dark'
    count = 0

    cleanupDir(output_folder)

    for file in files: 
        if file[-3:] != 'jpg': 
            continue 
        
        file_in = input_folder + file 
        file_out = output_folder + prefix + file 

        image = cv2.imread(file_in)
        result = image - (80,80,80)

        cv2.imwrite(file_out,result)
        count += 1
    return count 


def blur(input_folder, files):
    print('Blurring all the images from : ' + input_folder)

    output_folder = './blurred/'
    prefix = 'blur'
    count = 0

    cleanupDir(output_folder)

    for file in files: 
        if file[-3:] != 'jpg': 
            continue 
        
        file_in = input_folder + file 
        file_out = output_folder + prefix + file 

        image = cv2.imread(file_in)
        result = cv2.GaussianBlur(image, (7, 7), 0)

        cv2.imwrite(file_out,result)
        count += 1
    return count 


def grayscale(input_folder, files):
    print('Grayscaling all the images from : ' + input_folder)

    output_folder = './grayscaled/'
    prefix = 'gray'
    count = 0

    cleanupDir(output_folder)

    for file in files: 
        if file[-3:] != 'jpg': 
            continue 
        
        file_in = input_folder + file 
        file_out = output_folder + prefix + file 

        image = cv2.imread(file_in)
        result = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cv2.imwrite(file_out,result)
        count += 1
    return count 


def blackandwhite(input_folder, files):
    print('Black and whiting all the images from : ' + input_folder)

    output_folder = './blackandwhite/'
    prefix = 'bw'
    count = 0

    cleanupDir(output_folder)

    for file in files: 
        if file[-3:] != 'jpg': 
            continue 
        
        file_in = input_folder + file 
        file_out = output_folder + prefix + file 

        image = cv2.imread(file_in, cv2.IMREAD_GRAYSCALE)
        thresh = 128
        result = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]

        cv2.imwrite(file_out,result)
        count += 1
    return count 

 
def sepia(input_folder, files):
    print('Sepiaing all the images from : ' + input_folder)

    output_folder = './sepia/'
    prefix = 'sepia'
    count = 0

    cleanupDir(output_folder)

    for file in files: 
        if file[-3:] != 'jpg': 
            continue 
        
        file_in = input_folder + file 
        file_out = output_folder + prefix + file 

        image = cv2.imread(file_in)
        result = sepiaHelper(image)

        cv2.imwrite(file_out,result)
        count += 1
    return count 



def negative(input_folder, files):
    print('Negating all the images from : ' + input_folder)

    output_folder = './negative/'
    prefix = 'neg'
    count = 0

    cleanupDir(output_folder)

    for file in files: 
        if file[-3:] != 'jpg': 
            continue 
        
        file_in = input_folder + file 
        file_out = output_folder + prefix + file 

        image = cv2.imread(file_in)
        result = 1 - image

        cv2.imwrite(file_out,result)
        count += 1
    return count 

 
def rotate(input_folder, files, degree):
    print('Rotating all the images from : ' + input_folder)

    output_folder = './rotated/'
    prefix = 'rot'
    count = 0

    cleanupDir(output_folder)

    for file in files: 
        if file[-3:] != 'jpg': 
            continue 
        
        file_in = input_folder + file 
        file_out = output_folder + prefix + file 

        image = cv2.imread(file_in, cv2.IMREAD_GRAYSCALE)
        (rows, cols) = image.shape[:2]
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), degree, 1)    
        result = cv2.warpAffine(image, M, (cols, rows))

        cv2.imwrite(file_out,result)
        count += 1
    return count 

 
def brighten(input_folder, files):
    print('Brightening all the images from : ' + input_folder)

    output_folder = './brightened/'
    prefix = 'bright'
    count = 0

    cleanupDir(output_folder)

    for file in files: 
        if file[-3:] != 'jpg': 
            continue 
        
        file_in = input_folder + file 
        file_out = output_folder + prefix + file 

        image = cv2.imread(file_in)
        result = image + (80,80,80)

        cv2.imwrite(file_out,result)
        count += 1
    return count 


if __name__ == '__main__':

    # print("Getting the input parameters")

    parser = argparse.ArgumentParser(description="Checking project")
    parser.add_argument('--input_folder', type=str, default='./imgs1/', help='check images folder')
    
    args = parser.parse_args()
    input_folder = args.input_folder

    print("The input directory for images is: " + input_folder)

    files = os.listdir(input_folder)
    count = 0
    print(files)

    start = time.time()

    print('=========================================================')

    print('We would be performing following image-processing tasks on the images:')
    
    print('=========================================================')

    print('1. Blur an image')
    count = blur(input_folder, files)
    print(f'Blurred {count} images')

    print('=========================================================')
    print('2. Grayscale an image')
    count = grayscale(input_folder, files)
    print(f'Grayscaled {count} images')

    print('=========================================================')
    print('3. Black&White an image')
    count = blackandwhite(input_folder, files)
    print(f'Blacked and white {count} images')

    print('=========================================================')
    print('4. Sepia an image')
    count = sepia(input_folder, files)
    print(f'Sepiad {count} images')

    print('=========================================================')
    print('5. Negative an image')
    count = negative(input_folder, files)
    print(f'Negatived {count} images')

    print('=========================================================')
    print('6. Rotate an image')
    degree = 180
    count = rotate(input_folder, files, degree)
    print(f'Rotated {count} images by {degree} degree')

    print('=========================================================')
    print('7. Brighten an image')
    count = brighten(input_folder, files)
    print(f'Brightened {count} images')

    print('=========================================================')
    print('8. Darken an image')
    count = darken(input_folder, files)
    print(f'Darkened {count} images')

    print('=========================================================')
    end = time.time()
    diff = end - start 
    total = count * 8
    print(f'Took {diff} seconds for processing {total} images')
    print('=========================================================')
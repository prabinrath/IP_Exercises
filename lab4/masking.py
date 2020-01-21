import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import sys

image_or = cv2.imread(sys.argv[1],0)

def convolution_2d_corner(image,kernel): #corner convolution
    r,c = kernel.shape
    divisor = np.sum(kernel)
    y,x = image.shape
    y = y-r+1
    x = x-c+1
    output = np.zeros((y,x))
    if(r==c):
        for i in range(y):
            for j in range(x):
                output[i][j] = np.sum(np.multiply(image[i:i+r,j:j+c],kernel))/divisor
    else:
        print("Kernel should be square matrix")
    return output

def convolution_2d_centre(image,kernel): #centre convolution
    r,c = kernel.shape
    divisor = np.sum(kernel)
    y,x = image.shape
    startrow = int(r/2)
    startcol = int(c/2)
    rows = y-startrow+1
    cols = x-startcol+1
    output = np.zeros((y,x))
    if(r==c):
        for i in range(startrow,rows):
            for j in range(startcol,cols):
                output[i][j] = np.sum(np.multiply(image[i-startrow:i+startrow,j-startcol:j+startcol],kernel))/divisor
    else:
        print("Kernel should be square matrix")
    return output

kr1 = np.array([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])
kr2 = np.array([[1,2,2,1],[1,2,2,1],[1,2,2,1],[1,2,2,1]])
image_cv = convolution_2d_centre(image_or,kr2)

cv2.imshow("original",image_or)
cv2.imshow("convoluted",image_cv.astype('uint8'))
cv2.waitKey(0)
import cv2
import math
import numpy as np
from skimage.util import random_noise
from skimage.measure import compare_psnr as psnr
 
img = cv2.imread("cameraman.tif",0)
noise_img = random_noise(img, mode='s&p',amount=0.2)
noise_img = np.array(255*noise_img, dtype = 'uint8')

def median_filter(image,kernel): #centre convolution
    r = kernel[0]
    c = kernel[1]
    y,x = image.shape
    startrow = int(r/2)
    startcol = int(c/2)
    rows = y-startrow+1
    cols = x-startcol+1
    output = np.zeros((y,x))
    if(r==c):
        for i in range(startrow,rows):
            for j in range(startcol,cols):
                output[i][j] = np.median(image[i-startrow:i+startrow+1,j-startcol:j+startcol+1])
                #output[i][j] = np.mean(image[i-startrow:i+startrow+1,j-startcol:j+startcol+1])
                #output[i][j] = np.max(image[i-startrow:i+startrow+1,j-startcol:j+startcol+1])
                #output[i][j] = np.min(image[i-startrow:i+startrow+1,j-startcol:j+startcol+1])
    else:
        print("Kernel should be square matrix")
    output = np.array(output, dtype = 'uint8')
    return output

good_img = median_filter(noise_img,[3,3])

# mse_ni=0
# mse_gi=0
# for y in range(img.shape[0]):
#     for x in range(img.shape[1]):
#         mse_ni += (float(img[y][x])-float(noise_img[y][x]))**2
#         mse_gi += (float(img[y][x])-float(good_img[y][x]))**2
# mse_ni /= (img.shape[0]*img.shape[1])
# mse_gi /= (img.shape[0]*img.shape[1])
# print('PSNR of Noisy image: ',10*math.log10((255**2)/mse_ni))
# print('PSNR of Filtered image: ',10*math.log10((255**2)/mse_gi))

print('PSNR of Noisy image: ',psnr(img,noise_img))
print('PSNR of Filtered image: ',psnr(img,good_img))

cv2.imshow('noise image',noise_img)
cv2.imshow('median filter',good_img)
cv2.waitKey(0)
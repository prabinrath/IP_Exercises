import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
from skimage.measure import compare_psnr as psnr

def DCT(k,n,N):
    dct = -1
    if n==0:
        dct = np.sqrt(1/float(N))*np.cos((np.pi*(2*k+1)*n)/(2*float(N)))
    else:
        dct = np.sqrt(2/float(N))*np.cos((np.pi*(2*k+1)*n)/(2*float(N)))
    return dct

image = cv2.imread('cameraman.tif')
m=image.shape[0]
n=image.shape[1]
greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#generate A
complexMatrix = np.zeros((m,n),dtype= complex)
for i in range(0,m):
    for j in range(0,n):
        if j==0:
        	complexMatrix[i][j] = np.sqrt(1/float(m))*np.cos((np.pi*(2*i+1)*j)/(2*float(m)))
    	else:
        	complexMatrix[i][j] = np.sqrt(2/float(n))*np.cos((np.pi*(2*i+1)*j)/(2*float(n)))

#get the degraded image
conjMatrix = np.conj(complexMatrix)
dctImage = np.dot(np.dot((complexMatrix), greyImage ) , (np.transpose(conjMatrix)))
new_dctImage = np.zeros((m,n),dtype= complex)
k=100
new_dctImage[0:k][0:k] = dctImage[0:k][0:k]
idctImage = np.dot(np.dot((np.transpose(conjMatrix)), new_dctImage) , (complexMatrix))
plt.imshow(np.real(idctImage),cmap='gray')
print(image.shape,idctImage.shape)
print('PSNR of idct image: ',psnr(greyImage,idctImage))
plt.show()
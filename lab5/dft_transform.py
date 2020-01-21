import numpy
import cv2
import math
import matplotlib.pyplot as plt
from skimage.measure import compare_psnr as psnr

image = cv2.imread('cameraman.tif')
m=image.shape[0]
n=image.shape[1]
greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#generate A
complexMatrix = numpy.zeros((m,n),dtype= complex)
for i in range(0,m):
    for j in range(0,n):
        power = i*j
        real = math.cos((2*math.pi*power)/m)
        img = -math.sin((2*math.pi*power)/n)
        complexMatrix[i][j] = complex(real,img)

#get the degraded image
conjMatrix = numpy.conj(complexMatrix)
dftImage = numpy.dot(numpy.dot((complexMatrix), greyImage ) , (numpy.transpose(conjMatrix)))
idftImage = numpy.dot(numpy.dot((numpy.transpose(conjMatrix)), dftImage) , (complexMatrix))
plt.imshow(numpy.real(idftImage),cmap='gray')
print(image.shape,idftImage.shape)
print('PSNR of idft image: ',psnr(greyImage,idftImage))
plt.show()


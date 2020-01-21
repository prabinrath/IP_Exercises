import numpy
import cv2
import random
import math
import matplotlib.pyplot as plt

image = cv2.imread('cameraman.tif')
m=image.shape[0]
n=image.shape[1]
greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#generate A and H(u,v)
complexMatrix = numpy.zeros((m,n),dtype= complex)
blurMatrix = numpy.zeros((m,n),dtype=complex)
a = 0.001
b = 0.1
for i in range(0,m):
    for j in range(0,n):
        power = i*j
        real = math.cos((2*math.pi*power)/m)
        img = -1*math.sin((2*math.pi*power)/n)
        complexMatrix[i][j] = complex(real,img)

        blurMatrix[i][j] = numpy.exp(-1*(0.0001)*(5/6.0)*(i*i + j*j))

#get the degraded image
conjMatrix = numpy.conj(complexMatrix)
dftImage = numpy.matmul(numpy.matmul((complexMatrix),greyImage) , (numpy.transpose(complexMatrix)))
blurredImage = blurMatrix*dftImage
idftImage = numpy.matmul(numpy.matmul((numpy.transpose(conjMatrix)), blurredImage) , conjMatrix)
plt.imshow(numpy.real(idftImage),cmap='gray')
plt.show()

#restore the image
restoredImage = blurredImage/blurMatrix
idftImage = numpy.matmul(numpy.matmul((numpy.transpose(conjMatrix)), restoredImage) , conjMatrix)
plt.imshow(numpy.real(idftImage),cmap='gray')
plt.show()
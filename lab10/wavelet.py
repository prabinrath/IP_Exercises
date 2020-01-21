import numpy as np
import cv2
import random
import math
import matplotlib.pyplot as plt

img = cv2.imread('cameraman.tif')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = img.astype('float64')

q=0.7071068
hpf = [-q,q]
lpf = [q,q]

tempL = np.copy(img)
tempH = np.copy(img)
for x in range(img.shape[1]):
    for y in range(img.shape[0]):   #column wise
        if y<img.shape[0]-1:
            tempL[y][x] = img[y][x]*lpf[0]+img[y+1][x]*lpf[1]
            tempH[y][x] = img[y][x]*hpf[0]+img[y+1][x]*hpf[1]
        else:
            tempL[y][x] = img[y][x]*lpf[0]
            tempH[y][x] = img[y][x]*hpf[0]

reducedL = []
reducedH = []
for x in range(img.shape[1]):   #column reduction
    if x%2!=0:
        reducedL.append(tempL[:,[x]].flatten())
        reducedH.append(tempH[:,[x]].flatten())
reducedL = np.transpose(np.asarray(reducedL))
reducedH = np.transpose(np.asarray(reducedH))

tempLL = np.copy(reducedL)
tempLH = np.copy(reducedL)
tempHL = np.copy(reducedH)
tempHH = np.copy(reducedH)
for y in range(reducedL.shape[0]):
    for x in range(reducedL.shape[1]):   #row wise
        if x<reducedL.shape[1]-1:
            tempLL[y][x] = reducedL[y][x]*lpf[0]+reducedL[y][x+1]*lpf[1]
            tempLH[y][x] = reducedL[y][x]*hpf[0]+reducedL[y][x+1]*hpf[1]
            tempHL[y][x] = reducedH[y][x]*lpf[0]+reducedH[y][x+1]*lpf[1]
            tempHH[y][x] = reducedH[y][x]*hpf[0]+reducedH[y][x+1]*hpf[1]
        else:
            tempLL[y][x] = reducedL[y][x]*lpf[0]
            tempLH[y][x] = reducedL[y][x]*hpf[0]
            tempHL[y][x] = reducedH[y][x]*lpf[0]
            tempHH[y][x] = reducedH[y][x]*hpf[0]

reducedLL = []
reducedLH = []
reducedHL = []
reducedHH = []
for y in range(tempLL.shape[0]):    #row reduction
    if y%2==0:
       reducedLL.append(tempLL[y][:])
       reducedLH.append(tempLH[y][:])
       reducedHL.append(tempHL[y][:])
       reducedHH.append(tempHH[y][:])
reducedLL = np.asarray(reducedLL)
reducedLH = np.asarray(reducedLH)
reducedHL = np.asarray(reducedHL)
reducedHH = np.asarray(reducedHH)

fig=plt.figure(figsize=(2,2))
fig.add_subplot(2,2,1)
plt.imshow(reducedLL,cmap='gray')
fig.add_subplot(2,2,2)
plt.imshow(reducedLH,cmap='gray')
fig.add_subplot(2,2,3)
plt.imshow(reducedHL,cmap='gray')
fig.add_subplot(2,2,4)
plt.imshow(reducedHH,cmap='gray')
plt.show()

upsampledLL = []
upsampledLH = []
upsampledHL = []
upsampledHH = []
for y in range(reducedLL.shape[0]):    #row enhance
    upsampledLL.append(reducedLL[y])
    upsampledLL.append(reducedLL[y])
    upsampledLH.append(reducedLH[y])
    upsampledLH.append(reducedLH[y])
    upsampledHL.append(reducedHL[y])
    upsampledHL.append(reducedHL[y])
    upsampledHH.append(reducedHH[y])
    upsampledHH.append(reducedHH[y])
upsampledLL = np.asarray(upsampledLL)
upsampledLH = np.asarray(upsampledLH)
upsampledHL = np.asarray(upsampledHL)
upsampledHH = np.asarray(upsampledHH)

tempL = np.copy(upsampledLL)
tempH = np.copy(upsampledHH)
for y in range(upsampledLL.shape[0]):
    for x in range(upsampledLL.shape[1]):   #row wise
        if x<upsampledLL.shape[1]-1:
            tempL[y][x] = upsampledLL[y][x]*lpf[1]+upsampledLL[y][x+1]*lpf[0]+upsampledLH[y][x]*hpf[1]+upsampledLH[y][x+1]*hpf[0]
            tempH[y][x] = upsampledHL[y][x]*lpf[1]+upsampledHL[y][x+1]*lpf[0]+upsampledHH[y][x]*hpf[1]+upsampledHH[y][x+1]*hpf[0]
        else:
            tempL[y][x] = upsampledLL[y][x]*lpf[1]+upsampledLH[y][x]*hpf[1]
            tempH[y][x] = upsampledHL[y][x]*lpf[1]+upsampledHH[y][x]*hpf[1]

upsampledL = []
upsampledH = []
for x in range(tempL.shape[1]):   #column reduction
    upsampledL.append(tempL[:,[x]].flatten())
    upsampledL.append(tempL[:,[x]].flatten())
    upsampledH.append(tempH[:,[x]].flatten())
    upsampledH.append(tempH[:,[x]].flatten())
upsampledL = np.transpose(np.asarray(upsampledL))
upsampledH = np.transpose(np.asarray(upsampledH))

recon_img = np.copy(upsampledL)
for x in range(upsampledL.shape[1]):
    for y in range(upsampledL.shape[0]):   #column wise
        if y<upsampledL.shape[0]-1:
            recon_img[y][x] = upsampledL[y][x]*lpf[1]+upsampledL[y+1][x]*lpf[0]+upsampledH[y][x]*hpf[1]+upsampledH[y+1][x]*hpf[0]
        else:
            recon_img[y][x] = upsampledL[y][x]*lpf[1]+upsampledH[y][x]*hpf[1]

m,n=img.shape
sum_=0
for i in range(m):
    for j in range(n):
        sum_=sum_+(img[i][j]-recon_img[i][j])**2   

print('MSE is: ',sum_)
plt.imshow(recon_img,cmap='gray')
plt.show()
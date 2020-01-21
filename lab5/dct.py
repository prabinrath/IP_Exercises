import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
size = 16

def DCT(k,n,N):
    dct = -1
    if n==0:
        dct = np.sqrt(1/float(N))*np.cos((np.pi*(2*k+1)*n)/(2*float(N)))
    else:
        dct = np.sqrt(2/float(N))*np.cos((np.pi*(2*k+1)*n)/(2*float(N)))
    return dct

def getBasisDCT(a,b):
    b_image=[]
    for i in range(len(a)):
        temp=[]
        for j in range(len(b)):
            temp.append(a[i]*b[j])
        b_image.append(temp)
    return b_image

def basisImage(N):
    A_list=[]
    for i in range(N):
        Ak=[]
        for j in range(N):
            Ak.append(DCT(j,i,N))
        A_list.append(Ak)
    basis=[]
    for i in range(len(A_list)):
        temp=[]
        for j in range(len(A_list)):
            temp.append(getBasisDCT(A_list[i],A_list[j]))
        basis.append(temp)
    basis=np.asarray(basis)
    return basis

result=basisImage(size)
result[0][0][0][0]=0
fig=plt.figure(figsize=(size,size))
k=1
for i in range(size):
    for j in range(size):
        fig.add_subplot(size,size,k)
        plt.imshow(result[i][j],cmap='gray')
        k+=1
plt.show()
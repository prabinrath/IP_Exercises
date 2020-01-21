import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
size = 16

def DFT(k,n,N,arg):
    if arg==0:
        return np.cos((2*np.pi*k*n)/(float(N)))
    else:
        return -np.sin((2*np.pi*k*n)/(float(N)))

def getBasisDFT(a,b):
    b_image=[]
    for i in range(len(a)):
        temp=[]
        for j in range(len(b)):
            temp.append([a[i][0]*b[j][0]-a[i][1]*b[j][1],a[i][0]*b[j][1]+a[i][1]*b[j][0]])
        b_image.append(temp)
    return b_image

def basisImage(N,arg):
    A_list=[]
    for i in range(N):
        Ak=[]
        for j in range(N):
            Ak.append([DFT(j,i,N,0),DFT(j,i,N,1)])
        A_list.append(Ak)
    basis=[]
    for i in range(len(A_list)):
        temp=[]
        for j in range(len(A_list)):
            temp.append(getBasisDFT(A_list[i],A_list[j]))
        basis.append(temp)
    basis=np.asarray(basis)
    return basis

result=basisImage(size,0)
print(result.shape)

new_resr=[]
for i in range(size):
    temp1=[]
    for j in range(size):
        temp2=[]
        for k in range(size):
            temp3=[]
            for l in range(size):
                temp3.append(result[i][j][k][l][0]*255)
            temp2.append(temp3)
        temp1.append(temp2)
    new_resr.append(temp1)

new_resi=[]
for i in range(size):
    temp1=[]
    for j in range(size):
        temp2=[]
        for k in range(size):
            temp3=[]
            for l in range(size):
                temp3.append(result[i][j][k][l][1]*255)
            temp2.append(temp3)
        temp1.append(temp2)
    new_resi.append(temp1)

new_resr=np.asarray(new_resr)
new_resi=np.asarray(new_resi)

new_resr[0][0][0][0]=254
print(new_resr[0][0])
print(new_resi[0][0])

fig=plt.figure(figsize=(size,size))
k=1
for i in range(size):
    for j in range(size):
        fig.add_subplot(size,size,k)
        plt.imshow(new_resr[i][j],cmap='gray')
        k+=1
plt.show()

fig=plt.figure(figsize=(size,size))
k=1
for i in range(size):
    for j in range(size):
        fig.add_subplot(size,size,k)
        plt.imshow(new_resi[i][j],cmap='gray')
        k+=1
plt.show()

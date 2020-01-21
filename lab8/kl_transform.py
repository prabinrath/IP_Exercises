import numpy as np
import cv2
import random
import math
import matplotlib.pyplot as plt

image = cv2.imread('cameraman.tif')
m=image.shape[0]
n=image.shape[1]
greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cov_mat = np.cov(greyImage)
eigan_values, eigan_vectors = np.linalg.eig(cov_mat)

# k=1
# k_arr=[]
# mse_arr=[]
# while k<=256:
#     k_arr.append(k)
#     kl_mul = np.asarray(eigan_vectors[:,0:k])
#     compressed = np.matmul(np.transpose(kl_mul),greyImage)

#     restored = np.matmul(kl_mul,compressed)
#     mse_ri=0
#     for y in range(image.shape[0]):
#         for x in range(image.shape[1]):
#             mse_ri += (float(greyImage[y][x])-float(restored[y][x]))**2
#     mse_ri /= (greyImage.shape[0]*greyImage.shape[1])
#     mse_arr.append(mse_ri)
#     k+=1

# plt.plot(k_arr,mse_arr)
# plt.show()

k=10
kl_mul = np.asarray(eigan_vectors[:,0:k])
compressed = np.matmul(np.transpose(kl_mul),greyImage)

restored = np.matmul(kl_mul,compressed)
plt.imshow(restored,cmap='gray')
plt.show()
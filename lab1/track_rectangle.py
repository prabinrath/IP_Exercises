import cv2
import numpy as np
import matplotlib.pyplot as plt
height = 400
length = 500

mat = np.zeros((height, length))
x = 50
d = 30
for i in range(x, x+d):
    for j in range(x, length-x):
	    mat[i][j] = 1
for i in range(x+d, height-d-x):
    for j in range(x, x+d):
    	mat[i][j] = 1
    for j in range(length-x-d, length-x):
	    mat[i][j] = 1
for i in range(height-x-d, height-x):
	for j in range(x, length-x):
		mat[i][j] = 1
img = mat 
  
plt.imshow(img, cmap='gray') 
plt.show()

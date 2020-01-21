import cv2
import numpy as np
import math 
import matplotlib.pyplot as plt

height = 400
length = 500

mat = np.zeros((height, length))
r = 75
d = 20

mid_x = height/2
mid_y = length/2

for i in range(r, r+d):
    for angle in np.arange(0, 360, 0.01):
        x = mid_x+i*math.cos(angle)
        y = mid_y+i*math.sin(angle)
        mat[int(x)][int(y)] = 1

img = mat

plt.imshow(img, cmap='gray') 
plt.show()

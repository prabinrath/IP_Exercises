import math 
import matplotlib.pyplot as plt
import numpy as np
import cv2

height = 512
width = 512

img = np.zeros((height,width),dtype=np.uint8)

for i in range(0, height):
    for j in range(0, width):
        intensity = 255 * math.cos(2*3.1416*(float(i)/50 + float(j)/25))
        if(int(intensity)>=0):
            img[i, j] = int(intensity)

plt.imshow(img, cmap='gray')
plt.show()
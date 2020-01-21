import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("grain.png",0)

frq = np.zeros((256))   
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        frq[image[y][x]] = frq[image[y][x]] + 1

plt.bar(range(256), frq)
plt.show()

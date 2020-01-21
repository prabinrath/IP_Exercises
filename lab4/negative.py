import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import sys

image_or = cv2.imread(sys.argv[1],0)
image_ng = cv2.imread(sys.argv[1],0)

for y in range(image_or.shape[0]):
    for x in range(image_or.shape[1]):
        image_ng[y][x] = 255-image_or[y][x]

cv2.imshow("original",image_or)
cv2.imshow("negative",image_ng)
cv2.waitKey(0)
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

image_or = cv2.imread("tire.tif",0)
image_eq = cv2.imread("tire.tif",0)
image_ib = cv2.imread("tire.tif",0)

frq_or = np.zeros((256))
frq_eq = np.zeros((256))
frq_ib = np.zeros((256))

mapping = np.zeros((256))
cumulative = np.zeros((256))

for y in range(image_or.shape[0]):
    for x in range(image_or.shape[1]):
        frq_or[image_or[y][x]] = frq_or[image_or[y][x]] + 1

cumulative[0] = frq_or[0]
for i in range(1,256):
    cumulative[i] = cumulative[i-1]+frq_or[i]

cum = cumulative[255]

for i in range(256):
    cumulative[i] = cumulative[i]/cum

for i in range(256):
    mapping[i] = math.floor(cumulative[i]*255)

for y in range(image_eq.shape[0]):
    for x in range(image_eq.shape[1]):
        image_eq[y][x] = mapping[image_or[y][x]]

image_ib = cv2.equalizeHist(image_or)

for y in range(image_ib.shape[0]):
    for x in range(image_ib.shape[1]):
        frq_ib[image_ib[y][x]] = frq_ib[image_ib[y][x]] + 1

for y in range(image_eq.shape[0]):
    for x in range(image_eq.shape[1]):
        frq_eq[image_eq[y][x]] = frq_eq[image_eq[y][x]] + 1

plt.figure(1)
plt.subplot(211)
plt.bar(range(256), frq_eq)
plt.subplot(212)
plt.bar(range(256), frq_eq)
plt.show()

cv2.imshow("original",image_or)
cv2.imshow("equalized",image_eq)
cv2.waitKey(0)
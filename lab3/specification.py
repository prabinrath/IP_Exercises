import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

image_or = cv2.imread("tire.tif",0)
image_sp = cv2.imread("tire.tif",0)
image_tr = cv2.imread("cameraman.tif",0)

frq_or = np.zeros((256))
frq_sp = np.zeros((256))
frq_tr = np.zeros((256))

cumulative_or = np.zeros((256))
cumulative_tr = np.zeros((256))

#cumulative for input
for y in range(image_or.shape[0]):
    for x in range(image_or.shape[1]):
        frq_or[image_or[y][x]] = frq_or[image_or[y][x]] + 1

cumulative_or[0] = frq_or[0]
for i in range(1,256):
    cumulative_or[i] = cumulative_or[i-1]+frq_or[i]

cum = cumulative_or[255]

for i in range(256):
    cumulative_or[i] = cumulative_or[i]/cum
#########################

#cumulative for target
for y in range(image_tr.shape[0]):
    for x in range(image_tr.shape[1]):
        frq_tr[image_tr[y][x]] = frq_tr[image_tr[y][x]] + 1

cumulative_tr[0] = frq_tr[0]
for i in range(1,256):
    cumulative_tr[i] = cumulative_tr[i-1]+frq_tr[i]

cum = cumulative_tr[255]

for i in range(256):
    cumulative_tr[i] = cumulative_tr[i]/cum
##########################

#matching
j=0
index_map = np.zeros((256))
for i in range(256):
    this_val = cumulative_or[i]
    min_diff = abs(cumulative_or[i]-cumulative_tr[j])
    for k in range(j,256):
        new_diff = abs(cumulative_or[i]-cumulative_tr[j])
        if new_diff>min_diff:
            j = j-1
            break
        elif new_diff<=min_diff and j<255:
            j = j+1
    index_map[i] = j
#########################

for y in range(image_sp.shape[0]):
    for x in range(image_sp.shape[1]):
        image_sp[y][x] = index_map[image_or[y][x]]

for y in range(image_sp.shape[0]):
    for x in range(image_sp.shape[1]):
        frq_sp[image_sp[y][x]] = frq_sp[image_sp[y][x]] + 1

plt.figure(1)
plt.subplot(311)
plt.bar(range(256), frq_or)
plt.subplot(312)
plt.bar(range(256), frq_tr)
plt.subplot(313)
plt.bar(range(256), frq_sp)
plt.show()

cv2.imshow("original",image_or)
cv2.imshow("specified",image_sp)
cv2.waitKey(0)
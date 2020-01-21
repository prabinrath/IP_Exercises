import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("grain.png",0)

def bitStretching(img):
    ht = img.shape[0]
    wd = img.shape[1]
    img_bit = np.zeros((ht,wd), np.float64)
    
    for y in range(ht):
        for x in range(wd):
            if(img[y][x]>=0 and img[y][x]<80):
                img_bit[y][x] = img[y][x] * 0.5
            elif(img[y][x]>=80 and img[y][x]<160):
                img_bit[y][x] = img[y][x] * 2-120
            elif(img[y][x]>=160 and img[y][x]<200):
                img_bit[y][x] = img[y][x] * 0.57+107.52
    return img_bit

new_img = bitStretching(image)
plt.imshow(new_img,cmap='gray')
plt.show()

frq = np.zeros((256))   
for y in range(new_img.shape[0]):
    for x in range(new_img.shape[1]):
        frq[int(new_img[y][x])] = frq[int(new_img[y][x])] + 1

plt.bar(range(256), frq)
plt.show()
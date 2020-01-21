import cv2
import numpy as np
import matplotlib as plt

def bitSlicing(img,pos):
    ht = img.shape[0]
    wd = img.shape[1]
    img_bit = np.zeros((ht,wd), np.uint8)
    
    for y in range(ht):
        for x in range(wd):
            actual_val = np.binary_repr(img[y][x],width=8)
            if actual_val[pos] == '1':
                img_bit[y][x] = 255
            else:
                img_bit[y][x] = 0
    return img_bit

image = cv2.imread("fractal.png",0)

for i in range(8):
    sliced_img = bitSlicing(image,i)
    cv2.imshow("sample"+str(8-i),sliced_img)

cv2.waitKey(0)
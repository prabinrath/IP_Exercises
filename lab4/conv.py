import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('tire.tif',0)

def convolve2d(image, kernel):
    kernel = np.flipud(np.fliplr(kernel))
    output = np.zeros_like(image)
    image_padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2))   
    image_padded[1:-1, 1:-1] = image
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            output[y,x]=(kernel*image_padded[y:y+3,x:x+3]).sum()
    return output

plt.imshow(convolve2d(img,np.array([[1,1,1],[1,1,1],[1,1,1]],np.float64)/9),cmap='gray')
plt.show()
import math
import matplotlib.pyplot as plt
import numpy as np


def main():
    img = plt.imread('cameraman.tif')
    arr = np.asarray(img, dtype=np.uint8)
    row, col = arr.shape

    k = int(input('Enter zooming factor : '))
    
    img1 = np.zeros((int(row/k), int(col/k)), dtype=np.uint8)
    img2 = np.zeros((row * k, col * k), dtype=np.uint8)

    for i in range(len(img1)):
        for j in range(len(img1[0])):
            img1[i,j] = img[i*k,j*k];

    for i in range(len(img2)):
        for j in range(len(img2[0])):
            img2[i,j] = img[i/k,j/k];
    
    plt.imshow(img1, cmap="gray")
    plt.show()
    plt.imshow(img2, cmap="gray")
    plt.show()
    
if __name__ == "__main__":
    main()

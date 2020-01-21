import numpy as np
import cv2
import random
import math
import matplotlib.pyplot as plt
'''
image = cv2.imread('cameraman.tif')
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

frq = np.zeros((256))
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        frq[image[y][x]] = frq[image[y][x]] + 1

sum_ = 0
for i in range(256):
    sum_ = sum_ +frq[i]
for i in range(256):
    frq[i] = frq[i]/sum_

map_frq = {}
for i in range(256):
    map_frq[frq[i]] = i
hoff_map = {}
for i in sorted(map_frq):
    hoff_map[i] = map_frq[i]

values_s = []
frq_s = []
frq_bk = []
for i in hoff_map:
    frq_s.append(i)
    frq_bk.append(i)
    values_s.append(hoff_map[i])

for i in range(len(frq_s)):
    print(frq_s[i],values_s[i])

# frq_s.reverse()
values_s.reverse()
'''
values_s = [2,6,1,4,3,5]
frq_s = [0.04,0.06,0.1,0.1,0.3,0.4]
frq_bk = [0.04,0.06,0.1,0.1,0.3,0.4]

hoffmann_code = {}
ind = 0
def hoffmann(arr):
    global values_s,ind,hoffmann_code
    if len(arr)==2:
        hoffmann_code[values_s[ind]] = '1'
        ind = ind+1
        return '0'
    post_app = '1'
    post_ret = '0'
    if arr[0]==arr[1]:
        post_app = '0'
        post_ret = '1'
    temp = round(arr[0]+arr[1],15)
    del arr[0]; del arr[0];
    arr.append(temp)
    arr.sort()
    pred = hoffmann(arr)
    hoffmann_code[values_s[ind]] = pred+post_app
    ind = ind+1
    if ind==len(values_s)-1:
    	hoffmann_code[values_s[ind]] = pred+post_ret
    return pred+post_ret

pred = hoffmann(frq_s)
l_avg = 0
entropy = 0
for i in range(len(frq_bk)):
	l_avg += frq_bk[i]*len(hoffmann_code[values_s[i]])
	entropy += frq_bk[i]*math.log(frq_bk[i]+0.0000001)
	print(values_s[i],hoffmann_code[values_s[i]])

print('Length average: ',l_avg)
print('Entropy: ',-entropy)
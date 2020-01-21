import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from numpy import linalg
import operator
import math

prob = dict()
prob['a'] = 0.4
prob['b'] = 0.2
prob['c'] = 0.1
prob['d'] = 0.3

low_actual = dict()
high_actual = dict()
low_val = dict()
high_val = dict()

low_actual['a'] = 0
high_actual['a'] = prob['a']
low_val['a'] = 0
high_val['a'] = prob['a']

x = prob['a']
for i in prob:
    if(i == 'a'):
        continue;
    low_actual[i] = x
    low_val[i] = x
    high_actual[i] = x+prob[i]
    high_val[i] = x+prob[i]
    x = high_actual[i]
print(low_val)
print(high_val)

#for encoding
seq = "daada"
low = 0
high = 0
for i in range(len(seq)-1):
    low = low_val[seq[i]]
    high = high_val[seq[i]]
    rang = high-low
    for j in low_val:
        #print(low, rang, low_actual[j])
        low_val[j] = low + rang*low_actual[j]
        high_val[j] = low + rang*high_actual[j]
        
low = low_val[seq[len(seq)-1]]
high = high_val[seq[len(seq)-1]]
encoded_ans = (low+high)/2
print("Encoded output: ")
print(encoded_ans)


#for decoding
length = len(seq)
encoded = encoded_ans
ans = ""

tag = encoded
tag_new = 0
key = 'a'
for i in prob:
    if(tag>=low_actual[i] and tag<=high_actual[i]):
        ans = ans+i
        key = i
for i in range(length-1):
    tag = (tag-low_actual[key])/(high_actual[key]-low_actual[key])
    for j in prob:
        if(tag>=low_actual[j] and tag<=high_actual[j]):
            ans = ans+j
            key = j
print("Decoded output :")
print(ans)
#from math import prod
from itertools import product

filename='test.txt'
filename='input.txt'

data = open(filename).readlines()
test_list = [int(i) for i in data] 

for i in test_list:
    for j in test_list:
        if i+j==2020:
            k=i*j

print(k)

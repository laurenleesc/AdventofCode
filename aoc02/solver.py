#from math import prod
from itertools import product

#filename='test.txt'
filename='input.txt'

data = open(filename).readlines()

new_list=[]

for element in data:
    x = element.split()
    new_list.append(x)

count=0
for element in new_list:
    s=element[1].replace(':', '')
    t=element[2]
    u=element[0].split('-')
    v=list(map(int, u))

    occurrence=t.count(s)

    if occurrence in range (v[0],v[1]+1):
        count+=1

print(count)


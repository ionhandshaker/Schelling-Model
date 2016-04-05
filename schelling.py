
import numpy as np

import random as rand
size_of_array=40
import matplotlib.pyplot as plt

city=np.random.choice(3,size=(size_of_array,size_of_array),p=[0.2,0.4,0.4])


def is_unhappy(x,y,zone,n):
    k=5
    count=0
    temp=zone[x][y]
    if(temp==0):
        return False
    
    if(zone[x-1][y-1]==temp):
        count+=1
    if(zone[x][y-1]==temp):
        count+=1
    if(zone[(x+1)%n][y-1]==temp):
        count+=1
    if(zone[x-1][y]==temp):
        count+=1
    if(zone[(x+1)%n][y]==temp):
        count+=1
    if(zone[(x-1)][(y+1)%n]==temp):
        count+=1
    if(zone[x][(y+1)%n]==temp):
        count+=1
    if(zone[(x+1)%n][(y+1)%n]==temp):
        count+=1        
    #print count
    if(count>=k):
        return False
    else:
        return True
        
    
def find_empty(z,n):
    empty=[]
    for i in range(n):
        for j in range(n):
            if(z[i][j]==0):
                empty.append((i,j))
    return empty

def find_unhappy(z,n):
    unhappy=[]
    for i in range(n):
        for j in range(n):
            if(is_unhappy(i,j,z,n)):
                unhappy.append((i,j))
    return unhappy


   
number_of_passes=500
req=0
while req<number_of_passes:
    empty=find_empty(city,size_of_array)
    unhappy=find_unhappy(city,size_of_array)
    #print req,len(unhappy)
    if(len(empty)<len(unhappy)):
        for ch in range(len(empty)):
            current_unhappy=rand.choice(unhappy)
            current_empty=rand.choice(empty)
            city[current_empty[0]][current_empty[1]]=city[current_unhappy[0]][current_unhappy[1]]
            empty.remove(current_empty)
            city[current_unhappy[0]][current_unhappy[1]]=0
            unhappy.remove(current_unhappy)
    else:
        for ch in range(len(unhappy)):
            current_unhappy=rand.choice(unhappy)
            current_empty=rand.choice(empty)
            city[current_empty[0]][current_empty[1]]=city[current_unhappy[0]][current_unhappy[1]]
            empty.remove(current_empty)
            city[current_unhappy[0]][current_unhappy[1]]=0
            unhappy.remove(current_unhappy)
    req=req+1

#plt.plot(city)
plt.imshow(city,cmap=plt.cm.hot)
plt.colorbar()

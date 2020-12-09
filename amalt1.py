# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 07:44:54 2020

@author: amal
"""

file = open("input.txt", "r")
train_id=[]
edges=[]
nodes=set()

for line in file:
   m=line.split('/')
   train_id.append(m[0])
   edges.append(m[1:])
   u=set(m[1:])
   nodes.update(u)
  
   
file.close()

print(train_id)
print(edges)
print(nodes)

print(len(train_id))
print(len(edges))
print(len(nodes))
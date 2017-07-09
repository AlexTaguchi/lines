#!/usr/bin/env python3

from random_line import random_line

# generate points from two lines
points = []
xs, ys = random_line(2,2.9,0.15,size=40,start=-1,end=1)
for x,y in zip(xs,ys):
    points.append((x,y,1.0))
xs, ys = random_line(1,3.0,0.15,size=40,start=-1.1,end=1)
for x,y in zip(xs,ys):
    points.append((x,y,1.0))

with open('xys_2lines.txt','w') as f:
    for p in points:
        x,y,w = p
        f.write(str(x) + "," + str(y)  + "," + str(w) + "\n")

xs, ys = random_line(-0.1,3.1,0.1,size=40,start=-0.9,end=1.05)
for x,y in zip(xs,ys):
    points.append((x,y,1.0))

# generate additional one line
with open('xys_3lines.txt','w') as f:
    for p in points:
        x,y,w = p
        f.write(str(x) + "," + str(y)  + "," + str(w) + "\n")

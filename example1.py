#!/usr/bin/env python3

import numpy as np
import unittest
import scipy.stats
from lines.Lines import Lines
from lines.Point import Point
import matplotlib.pyplot as plt

# example of two lines

# First import sample data generated from two lines
data = np.loadtxt("data/xys_2lines.txt", delimiter=",")
# visualize the data
fig = plt.figure(figsize=(6,4))
plt.plot(data[:,0], data[:,1], 'k.')
#plt.savefig("data/two_lines_points_plots.png")
plt.show()

# prepare data for prediction
points = []
for d in data:
    x,y,w = d
    points.append(Point(x,y,w))

# make prediction
lines = Lines(penalty=0.5)  # user needs to tune penalty
lines.classify(points)
params = lines.get_coefficients()
for a, b, s in params:
    print("a: %.4f\tb: %.4f\tnumber_of_points: %d" % (a,b,s))

print("score: %.4f" % lines.get_score())

# visualize the lines
fig = plt.figure(figsize = (6,4))
colors = ['r','g','b','k','y']
for i in range(lines.number_of_lines()):
    s = lines.get_line(i)
    points = s.getPoints()
    a = s.a
    b = s.b
    xs = []
    ys = []
    for p in points:
        xs.append(p.x)
        ys.append(p.y)
    xs = np.array(xs)
    ys = np.array(ys)
    plt.plot(xs, a*xs + b, "-", color = colors[i], 
             label=("%.4f * x + %.4f" % (a,b)))
    plt.plot(xs, ys, ".", color = colors[i])
plt.legend()
#plt.savefig("data/two_lines_identified.png")
plt.show()



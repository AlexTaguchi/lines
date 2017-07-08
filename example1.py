#!/usr/bin/env python3

import numpy as np
import unittest
import scipy.stats
from lines.Lines import Lines
from lines.Segment import Segment
from lines.Segment import EvalPointError
from lines.Point import Point
import matplotlib.pyplot as plt


def random_line(m, b, sigma, size=10):
    xdata = np.linspace(-1,1,size)
    errors = scipy.stats.norm.rvs(loc=0,scale=sigma, size=size)
    ydata = m*xdata + b + errors
    return xdata, ydata

# example of a single line
xs, ys = random_line(2,3,0.1,size=20)
s = Segment()
for x, y in zip(xs,ys):
    p = Point(x,y,1.0)
    s.appendPoint(p)

a,b = s.a, s.b
print("\ny = a.x+b,\ta: %.4f\tb: %.4f" % (a,b))
print("RSS: %.4f" % s.calcRSS(s.a,s.b) )
fig = plt.figure(figsize = (8,6))
plt.plot(xs, ys, "b.")
plt.plot(xs, a*xs + b, "r-")
plt.show()

# example of two lines
points = []

xs, ys = random_line(2,2,0.15,size=40)
for x, y in zip(xs,ys):
    points.append(Point(x,y,1.0))
xs, ys = random_line(1,2,0.12,size=40)
for x, y in zip(xs,ys):
    points.append(Point(x,y,1.0))

lines = Lines(1.0)
lines.classify(points)
params = lines.get_coefficients()
for a, b, s in params:
    print("a: %.4f\tb: %.4f\tnumber_of_points: %d" % (a,b,s))

print("score: %.4f" % lines.get_score())
total_xs = []
total_ys = []
for p in points:
    total_xs.append(p.x)
    total_ys.append(p.y)

total_xs_np = np.array(total_xs)
total_ys_np = np.array(total_ys)

fig = plt.figure(figsize = (4,3))
plt.plot(total_xs, total_ys, "b.")
colors = ['r','g','b','k','y']
for a,b,s in params:
    plt.plot(total_xs_np, a*total_xs_np + b, "-", 
             label=("%.4f * x + %.4f" % (a,b)))
plt.legend()
#plt.savefig("data/lines.png")
plt.show()



#!/usr/bin/env python3

import numpy as np
import unittest
import scipy.stats
from lines.Lines import Lines
from lines.Segment import Segment
from lines.Point import Point

def random_line(m, b, sigma, size=10):
    xdata = np.linspace(-1,1,size)
    errors = scipy.stats.norm.rvs(loc=0,scale=sigma, size=size)
    ydata = m*xdata + b + errors
    return xdata, ydata

class SegmentProperties(unittest.TestCase):
    def test_construct_segment(self):
        seg = Segment()

    def test_Segment_regression(self):
        xs, ys = random_line(2,3,0.1,size=20)
        s = Segment()
        for x, y in zip(xs,ys):
            p = Point(x,y,1.0)
            s.appendPoint(p)
        
        a,b = s.a, s.b
        print("\ny = a.x+b,\ta: %.4f\tb: %.4f" % (a,b))
        print("RSS: %.4f" % s.calcRSS(s.a,s.b) )
        

    def test_Lines_initiation(self):
        print("Predict segments of lines:")
        xs, ys = random_line(2,3,0.1,size=20)
        points = []
        for x, y in zip(xs,ys):
            points.append(Point(x,y,1.0))
        xs, ys = random_line(1,5,0.1,size=20)
        for x, y in zip(xs,ys):
            points.append(Point(x,y,1.0))

        lines = Lines(1.0)
        lines.classify(points)
        params = lines.get_coefficients()
        for a, b, s in params:
            print("a: %.4f\tb: %.4f\tnumber_of_points: %d" % (a,b,s))

        print("score: %.4f" % lines.get_score())
        

if __name__ == '__main__':
    unittest.main()

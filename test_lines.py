#!/usr/bin/env python3

import numpy as np
import unittest
import scipy.stats
from lines.Lines import Lines
from lines.Segment import Segment
from lines.Segment import EvalPointError
from lines.Point import Point

def random_line(m, b, sigma, size=10):
    xdata = np.linspace(-1,1,size)
    errors = scipy.stats.norm.rvs(loc=0,scale=sigma, size=size)
    ydata = m*xdata + b + errors
    return xdata, ydata

class SegmentTestCase(unittest.TestCase):
    def test_construct_segment(self):
        seg = Segment()
        self.assertAlmostEqual(seg.a, 0, 10)
        self.assertAlmostEqual(seg.b, 0, 10)
        self.assertRaises(EvalPointError, seg.evalPoint, Point(1,1,1.0))

    def test_appendPoint(self):
        # first line y = x
        seg = Segment()
        pt1 = Point(1,1,1.0)
        seg.appendPoint(pt1)
        self.assertAlmostEqual(seg.a, 0, 10)
        self.assertAlmostEqual(seg.b, 0, 10)

        pt2 = Point(4,4,1.0)
        seg.appendPoint(pt2)
        self.assertAlmostEqual(seg.a, 1.0, 10)
        self.assertAlmostEqual(seg.b, 0.0, 10)
        self.assertAlmostEqual(seg.calcRSS(seg.a,seg.b), 0.0, 10)

        pt3 = Point(10,10,1.0)
        seg.appendPoint(pt3)
        self.assertAlmostEqual(seg.a, 1.0, 10)
        self.assertAlmostEqual(seg.b, 0.0, 10)
        self.assertAlmostEqual(seg.calcRSS(seg.a,seg.b), 0.0, 10)

        # second line y = 2x + 1
        seg2 = Segment()
        pt2_1 = Point(0,1,1.0)
        seg2.appendPoint(pt2_1)
        pt2_2 = Point(3,7,1.0)
        seg2.appendPoint(pt2_2)
        self.assertAlmostEqual(seg2.a, 2.0, 10)
        self.assertAlmostEqual(seg2.b, 1.0, 10)
        self.assertAlmostEqual(seg2.calcRSS(seg2.a,seg2.b), 0.0, 10)

    def test_calcRSS(self):
        s = Segment()
        s.appendPoint(Point(1,1,1))
        s.appendPoint(Point(1,2,1))
        s.appendPoint(Point(2,1,1))
        s.appendPoint(Point(2,2,1))
        self.assertAlmostEqual(s.a, 0.0, 10)
        self.assertAlmostEqual(s.b, 1.5, 10)

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

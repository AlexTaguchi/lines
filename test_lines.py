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
        self.assertAlmostEqual(0, seg.a, 10)
        self.assertAlmostEqual(0, seg.b, 10)
        self.assertRaises(EvalPointError, seg.evalPoint, Point(1,1,1.0))

    def test_appendPoint(self):
        # first line y = x
        seg = Segment()
        pt1 = Point(1,1,1.0)
        seg.appendPoint(pt1)
        self.assertAlmostEqual(0, seg.a, 10)
        self.assertAlmostEqual(0, seg.b, 10)

        pt2 = Point(4,4,1.0)
        seg.appendPoint(pt2)
        self.assertAlmostEqual(1.0, seg.a, 10)
        self.assertAlmostEqual(0.0, seg.b, 10)
        self.assertAlmostEqual(0.0, seg.calcRSS(seg.a,seg.b), 10)

        pt3 = Point(10,10,1.0)
        seg.appendPoint(pt3)
        self.assertAlmostEqual(1.0, seg.a, 10)
        self.assertAlmostEqual(0.0, seg.b, 10)
        self.assertAlmostEqual(0.0, seg.calcRSS(seg.a,seg.b), 10)

        # second line y = 2x + 1
        seg2 = Segment()
        pt2_1 = Point(0,1,1.0)
        seg2.appendPoint(pt2_1)
        pt2_2 = Point(3,7,1.0)
        seg2.appendPoint(pt2_2)
        self.assertAlmostEqual(2.0, seg2.a, 10)
        self.assertAlmostEqual(1.0, seg2.b, 10)
        self.assertAlmostEqual(0.0, seg2.calcRSS(seg2.a,seg2.b), 10)

    def test_calcRSS(self):
        s = Segment()
        s.appendPoint(Point(1,1,1))
        s.appendPoint(Point(1,2,1))
        s.appendPoint(Point(2,1,1))
        s.appendPoint(Point(2,2,1))
        self.assertAlmostEqual(0.0, s.a, 10)
        self.assertAlmostEqual(1.5, s.b, 10)

class LinesTestCases(unittest.TestCase):
    def test_init(self):
        l = Lines()
        self.assertAlmostEqual(0.0, l.get_score(), 10)
        self.assertAlmostEqual(1.0, l.penalty, 10)
        self.assertEqual(0, l.number_of_lines())

    def test_addPoint(self):
        l = Lines()
        l.addPoint(Point(1,1,1))
        l.addPoint(Point(4,4,1))
        params = l.get_coefficients()
        self.assertEqual(1, len(params))
        a,b,s = params[0]
        self.assertEqual(2, s)
        self.assertAlmostEqual(1.0, a, 10)
        self.assertAlmostEqual(0.0, b, 10)


if __name__ == '__main__':
    unittest.main()

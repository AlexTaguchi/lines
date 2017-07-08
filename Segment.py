#!/usr/bin/env python3

import numpy as np
from lines.Point import Point

class Segment:
    def __init__(self):
        self.a = 0  # y = a.x + b
        self.b = 0
        self._points = []
        self._rss = 0  # Residual sum of squares
        self._wixiyi = 0
        self._wixi = 0
        self._wiyi = 0
        self._wixi2 = 0
        self._wi = 0

    def getLength(self):
        return len(self._points)

    def appendPoint(self, p):
        self._points.append(p)
        self._wixiyi += p.w * p.x * p.y
        self._wixi += p.w * p.x
        self._wiyi += p.w * p.y
        self._wixi2 += p.w * p.x * p.x
        self._wi += p.w
        if len(self._points)>1:
            self.a = (self._wixiyi - self._wixi*self._wiyi/self._wi)/(self._wixi2 \
                    - self._wixi**2/self._wi)
            self.b = (self._wiyi - self.a * self._wixi)/self._wi
            self._rss = self.calcRSS(self.a, self.b)

    def calcRSS(self, a, b):
        """ calculate Residual Sum of Squares
        
        Args:
            a (float): slope
            b (float): intercept

        Returns:
            float: residual sum of squares
        """
        rss = 0
        for p in self._points:
            rss += p.w * (p.y - a * p.x - b)**2

        return rss
        
    def evalPoint(self, p):
        """calculate a and b of y=a.x+b before including in the point p

        Args:
            p (Point): a point not in Segment
        
        Returns:
            (a,b): a tuple for slope and intercept for fitted line y=a.x+b
        """
        if not self._points:
            raise ValueError("""Cannot calculate slope 
                        and intercept with a single point.
                      """)
        x = p.x
        y = p.y
        w = p.w

        wixiyi = self._wixiyi + w*x*y
        wixi = self._wixi + w*x
        wiyi = self._wiyi + w*y
        wixi2 = self._wixi2 + w*x*x
        wi = self._wi + w

        a = (wixiyi - wixi*wiyi/wi)/(wixi2 - wixi**2/wi)
        b = (wiyi - a * wixi)/wi
        return (a,b)

    def evalRSS(self, p):
        new_a, new_b = self.evalPoint(p)
        rss = self.calcRSS(new_a, new_b)
        rss += p.w * (p.y - self.a * p.x - self.b)**2
        return rss
        


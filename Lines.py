#!/usr/bin/env python3

from lines.Segment import Segment
from lines.Point import Point
import sys

class Lines:
    """
    class Lines looks for possible lines among a set of points with weights.
    """
    def __init__(self, penalty=1.0):
        self._segments = []
        self._score = 0
        self.penalty = 1.0  # penalty for add a new segment

    def get_score(self):
        return self._score

    def get_coefficients(self):
        params = []
        for s in self._segments:
            a,b = s.a, s.b
            params.append((a,b))
        return params

    def set_penalty(self, p):
        self.penalty = p
    
    def addPoint(self,p):
        if not self._segments:
            s = Segment()
            s.appendPoint(p)
            self._segments.append(s)
            return
            
        new_err = sys.float_info.max # initial value
        belong_to = -1 
        
        for i, s in enumerate(self._segments):
            original_err = s.calcRSS(s.a, s.b)
            potential_err = s.evalRSS(p)
            diff_err = potential_err - original_err
            if diff_err < new_err:
                new_err = diff_err
                belong_to = i

        if new_err < penalty and belong_to > -1:
            self._segments[belong_to].appendPoint(p)
            self._score += new_err
        else:
            s = Segment()
            s.appendPoint(p)
            self._segments.append(p)
            self._score += penalty
        

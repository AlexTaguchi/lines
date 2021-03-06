#!/usr/bin/env python3

from lines.Segment import Segment
import sys

class LineIndexOutOfRange(ValueError):
    pass


class Lines:
    """
    class Lines looks for possible lines among a set of points with weights.
    """
    def __init__(self, penalty=1.0):
        self._segments = []
        self._score = 0
        self.penalty = penalty  # penalty for add a new segment

    def get_score(self):
        """get score for fitting. Smaller number is preferred"""
        return self._score

    def get_coefficients(self):
        """ return tuples of a,b, and size"""
        params = []
        for s in self._segments:
            a, b = s.a, s.b
            sz = s.getLength()
            params.append((a, b, sz))
        return params

    def get_line(self, i):
        """return the indexed line"""
        if i >= len(self._segments):
            raise LineIndexOutOfRange("index too large")

        return self._segments[i]
        

    def number_of_lines(self):
        return len(self._segments)

    def set_penalty(self, p):
        """ update penalty for adding a new line
            The higher the value, the less likely a new line.
        """
        self.penalty = p

    def classify(self, points):
        """ classify points into corresponding lines"""
        for p in points:
            self.addPoint(p)

    def addPoint(self, p):
        """ classify a point to existing lines,
            or create a new line(Segment)
        """
        if len(self._segments) < 1:
            s = Segment()
            s.appendPoint(p)
            self._segments.append(s)
            return

        new_err = sys.float_info.max  # initial value
        belong_to = -1

        for i, s in enumerate(self._segments):
            original_err = s.calcRSS(s.a, s.b)
            potential_err = s.evalRSS(p)
            diff_err = potential_err - original_err
            if diff_err < new_err:
                new_err = diff_err
                belong_to = i

        if new_err < self.penalty and belong_to > -1:
            self._segments[belong_to].appendPoint(p)
            self._score += new_err
        else:
            s = Segment()
            s.appendPoint(p)
            self._segments.append(s)
            self._score += self.penalty

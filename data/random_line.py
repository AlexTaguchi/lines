#!/usr/bin/env python3

import numpy as np
import scipy.stats

def random_line(a, b, sigma, size=10):
    """random_line() generate random points arround y=a*x+b,
    with normal distribution defined using sigma"""
    xdata = np.linspace(-1,1,size)
    errors = scipy.stats.norm.rvs(loc=0,scale=sigma, size=size)
    ydata = a*xdata + b + errors
    return xdata, ydata

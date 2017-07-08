# Lines

Identify multiple lines among a set of points.
-----------------------------------------------

![Two lines were identified in this set of points.](data/lines.png)

Background
==========

It is sometimes required that multiple lines can be extracted from an ensemble of points. This package provides a simple method in dealing with such classification problem. 

A point is defined as a three element tuple *(x,y,weight)*. And each line is associated with a slope **a** and an intercept **b**. We can define the *Residual Sum of Squares* (RSS) of weighted points by taking the weight into account as well. a and b can be calculated by equal gradient of RSS to zero. 

However, when multiple lines are presented, one needs to evaluate the RSS of each line to determine which one a point belongs to.


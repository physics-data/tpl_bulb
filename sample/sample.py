#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
# This line indicate a PNG backend, thus no need for X server
matplotlib.use('agg')
import matplotlib.pyplot as plt

xvals = np.arange(-1, 1, 1e-5)

def upper(x):
    ax = abs(x)
    if ax <= 1:
        return np.sqrt(1 - ax ** 2)
    else:
        return np.nan

def down(x):
    ax = abs(x)
    if ax <= 1 and ax >= 1/2:
        return - np.sqrt(1 - ax ** 2)
    else:
        return np.nan

def neck(x):
    ax = abs(x)
    if ax >= 0.2 and ax <= 0.5:
        return np.sqrt(0.6 ** 2 - (ax - 0.8) ** 2) -\
            np.sqrt(1.6 ** 2 - 0.8 ** 2)
    else:
        return np.nan

plt.plot(xvals, list(map(upper, xvals)), color='y')
plt.plot(xvals, list(map(down, xvals)), color='y')
plt.plot(xvals, list(map(neck, xvals)), color='y')
plt.xlim(-1.2,1.2)
plt.ylim(-1.7,1.2)
# The following line is used for create equal scale x,y axes
plt.gca().set_aspect('equal',adjustable='box')
plt.savefig('bulb.png')

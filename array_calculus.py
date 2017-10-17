#!/usr/bin/env python3
# Name: Nikki Schwartz and Riley Kendall
# Student ID: 2267883
# Email: schwa218@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 6

import numpy as np

def derivative(a,b,n):
    dx = (b-a)/(n-1)
    D = np.eye(n,n,1)-np.eye(n,n,-1)
    D[0][0] = -2
    D[0][1] = 2
    D[-1][-1] = 2
    D[-1][-2] = -2
    D = D/(2*dx)
    return D
def second_derivative(a,b,n):
    

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:24:15 2019

@author: Nikhil Tank
Comp Architecture code for vector addition in CUDA fro power 
"""
import numpy as np
from timeit import default_timer as timer
from numba import vectorize

@vectorize(['float32(float32, float32)'], target='cuda')
def addition(a, b):
    return a + b

def main():
    vec_size = 100000000

    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    c = np.zeros(vec_size, dtype=np.float32)

    start = timer()
    c = addition(a, b)
    duration = timer() - start

    print("vector add time take : ",duration)

if __name__ == '__main__':
    main()

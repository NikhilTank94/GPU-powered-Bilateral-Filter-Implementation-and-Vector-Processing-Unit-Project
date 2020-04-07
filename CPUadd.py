# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 22:00:28 2019

@author: Nikhil Tank

no parallism code
"""
import numpy as np
from timeit import default_timer as timer



def main():
    vec_size = 100000000

    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    c = np.zeros(vec_size, dtype=np.float32)

    start = timer()
    np.matmul(a, b)
    duration = timer() - start

    print(duration)

if __name__ == '__main__':
    main()

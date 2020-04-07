# -*- coding: utf-8 -*-
"""
* Bilateral filter
* Need to reduce the size of the images to say (64,64) before applying the bilateral ﬁlter otherwise, 
* Else, the ﬁltering operation can be very slow
"""
import cv2
import numpy as np
from timeit import default_timer as timer

img = cv2.imread('cent.jpg')
m, n = 480, 480
f = cv2.resize(img, (m,n))
cv2.imwrite('cent_resize.jpg',f)

sig_d = 10
sig_r = 50

g = np.zeros(f.shape, dtype = np.uint8)
d = np.zeros((7,7))
start = timer()
for k in range (0,7):
    for l in range (0,7):
        d[k][l] = np.exp(-((k-3)**2 + (l-3)**2)/(2*(sig_d**2)) )
        
for z in range(0,3):
    for i in range (0,m):
        for j in range (0,n):            
            w,r,a,b = 0,0,0,0
            #r = np.zeros((11,11))
            for k in range (0,7): #using a reduced kernel size
                for l in range (0,7):
                    if i-k+3 >= 0 and i-k+3 < m and j-l+3 >= 0 and j-l+3 < n:
                        r = np.exp(-((f[i,j,z]-f[i-k+3,j-l+3,z])**2)/(2*(sig_r**2)) )
                        w = r*d[k][l]
                        a = a + f[i-k+3,j-l+3,z]*w
                        b = b + w
            g[i,j,z] = round(a/b)       
duration = timer() - start
print("bilateral filter time take : ",duration)
cv2.imwrite('face_bfltr_CPU.jpg',g)

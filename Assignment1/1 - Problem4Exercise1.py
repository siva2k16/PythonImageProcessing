#1.Plot all the intensities in A, sorted in decreasing value
#		30/08/2015		Draft Version

import cv2
import numpy as np
from matplotlib import pyplot as plt

#0 will load grey image
sourcegreyimg = cv2.imread('einstein.jpg',0)

#ravel - Return a flattened array
plt.hist(sourcegreyimg.ravel(),256,[0,256]);
plt.show()

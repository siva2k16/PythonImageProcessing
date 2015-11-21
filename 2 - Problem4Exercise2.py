#2. Display a histogram of A's intensities with 20 bins
#	30/08/2015		Draft Version

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Load Image
sourceimg = cv2.imread('einstein.jpg',0)

#Specify 20 bins
plt.hist(sourceimg.ravel(),20,[0,256]);
plt.show()

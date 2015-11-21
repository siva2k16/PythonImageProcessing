#Find max pixel position and assign to row and column
#	30/08/2015		Draft Version
import cv2
import numpy as np
from matplotlib import pyplot as plt

sourceimg = cv2.imread('einstein.jpg',0)

#Find the min. max location of pixel with location and value
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(sourceimg)

row_loc = max_loc[0]
col_loc = max_loc[1]

print 'RowLocation'
print row_loc
print 'Column Location'
print col_loc
print 'Max Value'
print max_val


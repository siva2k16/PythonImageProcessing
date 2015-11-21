# With 3 channels to represent R G and B values
#wherever the intensity in A is greater than a threshold t, and black everywhere else
#30/08/2015		Draft Version
import cv2
import Image
import numpy as np

#Load Gray Scale Image
sourceImage = cv2.imread('einstein.jpg', 0)

#Compute Mean of Grayscale Image
frame_mean = np.sum(sourceImage) / float(sourceImage.shape[0] * sourceImage.shape[1])

#Set Threshold where value greater then mean
ret,destthreshold = cv2.threshold(sourceImage,frame_mean,255,cv2.THRESH_BINARY)

#Convert Gray to color
destimg = cv2.cvtColor( destthreshold, cv2.COLOR_GRAY2RGB)

#Set B channel to Zero
destimg[:,:,0] = 0

#Set G channel to Zero
destimg[:,:,1] = 0

#Output Mean Value
print frame_mean
cv2.imshow('ThresholdApplied',destimg)
cv2.waitKey(0)


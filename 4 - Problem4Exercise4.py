#4. Create a new image X that consists of the bottom left quadrant of A. 
#	30/08/2015		Draft Version
#Image Load, Identify Coordinates
#Crop the Image
#Save Cropped Image

import cv2
from matplotlib import pyplot as plt

#Load Image
sourceImage = cv2.imread('einstein.jpg')
row = sourceImage.shape[0]
column = sourceImage.shape[1]

#Identify Coordinates to split
rowstart = row/2
rowend = row
column = column/2

#Fetch left most quadrant of image
destImage = sourceImage[rowstart:rowend,0:column]
cv2.imshow('cropped',destImage)
cv2.waitKey(0)

#Image will be saved only in working directory
cv2.imwrite('result.jpg',destImage)
cv2.waitKey(0)

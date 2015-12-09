#       About - Cross Correlation and identify matching template from source image
#       Updated             11/10/2015
#       Load the input image
#       Based on the template image create blocks     
#       Compute NCC and save coordinates where NCC is max value
#       Output regions where the matching corrdinates are found
#       Output for first template, close it, continue with next set

import cv2
import numpy as np
import math as m
import timeit

#Load Input Image
sourceImage = cv2.imread('u2cuba.jpg')
sourceImage = cv2.cvtColor(sourceImage,cv2.COLOR_BGR2GRAY)

#Cross Correlation function
def computeCrossCorrelation(inputimage, templateImage1):
	#Compute width and height of Input Image
	width = sourceImage.shape[0]
	height = sourceImage.shape[1]

	#Compute width and height of template Image
	width1 = templateImage1.shape[0]
	height1 = templateImage1.shape[1]

	#Initialze current Ncc value to zero
	currdist_ncc1 = 0

	#Create destination output each
	destNewImageTemp = sourceImage[0:width1,0:height1]

	#Loop thru width of Image
	for x in range(0,width,1):
		
		#Loop through height of Image
		for y in range(0,height,1):

			#Check if pixel position input image + dimension of template image are within limits
			if (x+width1 < width and y+height1< height):

				#Pick the block matching dimension of template image
				destNewImageTemp = sourceImage[x:x+width1,y:y+height1]

				#Compute Ncc for the Identified block
				dist_ncc1 = sum((templateImage1-np.mean(templateImage1))*(destNewImageTemp-np.mean(destNewImageTemp)))/m.sqrt((np.std(templateImage1)*np.std(destNewImageTemp)))

				#If sum > current sum, capture value and coordinates
				if ((sum(dist_ncc1) > currdist_ncc1) and (sum(dist_ncc1)> 0)):
					currdist_ncc1 = sum(dist_ncc1)
					matchCoordwidth = x
					matchCoordwidth1 = x+width1
					matchCoordHeight = y
					matchCoordHeight1 = y+height1

	destMatchImageTemp = sourceImage[matchCoordwidth:matchCoordwidth1,matchCoordHeight:matchCoordHeight1]

	#Template Image
	cv2.imshow('Template Image',templateImage1)

	#Matched Area
	cv2.imshow('Result Image Extracted portion is ',destMatchImageTemp)

	#Highlight from input Image
	cv2.rectangle(sourceImage, (matchCoordHeight, matchCoordwidth),(matchCoordHeight1,matchCoordwidth1), (255,0,0), 2)
	cv2.imshow("Highlighted Section is white is matching image", sourceImage)

	print 'Please verify and close this output to proceed with next data set'

#Load template Image to search
#Part A 
templateImage1 = cv2.imread('trailer.png')
templateImage1 = cv2.cvtColor(templateImage1,cv2.COLOR_BGR2GRAY)

#start timer - Inbuilt function
start = timeit.default_timer()

computeCrossCorrelation(sourceImage,templateImage1)

print 'Template smaller image - time to find - in seconds '
stop = timeit.default_timer()
print stop-start 
cv2.waitKey(0)    


#Load large template Image to Search
#Part B
sourceImage = cv2.imread('u2cuba.jpg')
sourceImage = cv2.cvtColor(sourceImage,cv2.COLOR_BGR2GRAY)
templateImage2 = cv2.imread('trailerSlightlyBigger.png')
templateImage2 = cv2.cvtColor(templateImage2,cv2.COLOR_BGR2GRAY)

#start timer - Inbuilt function
start = timeit.default_timer()

computeCrossCorrelation(sourceImage,templateImage2)

print 'Template larger image - time to find - in seconds'
stop = timeit.default_timer()
print stop-start 

cv2.waitKey(0)    

#       Load the Image, Compute value for each position by applying kernel filter
#       If val < 0 then make obtained value =  zero, If val > 255 then make obtained value = 255
#       Substitute Val at Pixel location 255-obtained value
import cv2
import numpy as np
import math as m
import timeit

#Load Image
sourceImage = cv2.imread('u2cuba.jpg')
sourceImage = cv2.cvtColor(sourceImage,cv2.COLOR_BGR2GRAY)

#start timer
start = timeit.default_timer()

#Laplacian Filter
Laplacian = np.array([ [1,1,1],[1,-8,1],[1,1,1]],np.float32)

width = sourceImage.shape[0]
height = sourceImage.shape[1]

destImage = sourceImage[0:width,0:height]

for y in range(1,height-1):
    for x in range(1,width-1):
        destImage[x][y] = 0
        row1Val = 0
        row2Val = 0
        row3Val = 0
        
        #Multiple by 1,1,1
        row1Val = (Laplacian[0][0]*sourceImage[x-1,y-1])+(Laplacian[0][1]*sourceImage[x-1,y])+(Laplacian[0][2]*sourceImage[x-1,y+1])

        #Multiple by 1,-8,1
        row2Val = (Laplacian[1][0]*sourceImage[x,y-1])+(Laplacian[1][1]*sourceImage[x,y])+(Laplacian[1][2]*sourceImage[x,y+1])
    
        #Multiple by 1,1,1
        row3Val = (Laplacian[2][0]*sourceImage[x+1,y-1])+(Laplacian[2][1]*sourceImage[x+1,y])+(Laplacian[2][2]*sourceImage[x+1,y+1])

        #Sum the value obtained for all 3 rows
        resultValue = row1Val+row2Val+row3Val

        #Check for limits 255 and 0
        if(resultValue > 255):
            resultValue = 255
            
        if(resultValue < 0):
            resultValue = 0
        
        #print 255-resultValue
        destImage[x][y] = 255-resultValue
        
cv2.imshow('Laplacian Code Output',destImage)

print 'Laplacian - time to compute - custom code - in seconds'
stop = timeit.default_timer()
print stop-start 

#start timer - Inbuilt function
start = timeit.default_timer()
laplacian = cv2.Laplacian(sourceImage,cv2.CV_64F)

print 'Laplacian - time to compute - Inbuilt function - in seconds'
stop = timeit.default_timer()
print stop-start 

cv2.imshow('Laplacian Function Output',laplacian)
cv2.waitKey(0)

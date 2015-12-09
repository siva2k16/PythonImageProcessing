#       About - Applying Sobel Filter for given Input Image
#       Updated                     07/10/2015
#       Load the Image, Compute Gradient Gx and Gy on input image
#       Absolute magnitude is obtained by sqrt(gx square and gy square)
#       If value > 255 replace with 255, If < 0 replace with zero else apply computed value

import cv2
import numpy as np
import math as m
import timeit
from matplotlib import pyplot as plt

#Load the Input Image
sourceImage = cv2.imread('u2cuba.jpg')

#start timer
start = timeit.default_timer()

#Convert it to Grayscale
sourceImage = cv2.cvtColor(sourceImage,cv2.COLOR_BGR2GRAY)

#Initialize Sonel Gx and Gy Filters
sobelx = np.array([ [-1,0,1],[-2,0,2],[-1,0,1]],np.float32)
sobely = np.array([ [-1,-2,-1],[0,0,0],[1,2,1]],np.float32)

#Compute width and Height of Image
width = sourceImage.shape[0]
height = sourceImage.shape[1]

#Create Destination Image
destImage = sourceImage[0:width,0:height]

#Loop until 1 to Width of Image
for x in range(1,width-2):
    
    #Loop until 1 to Height of Image
    for y in range(1,height-2):

        #Initialize Destination Pixel value to Zero
        destImage[x][y] = 0

        #Compute Gx
        Gx = (sobelx[0][0]*sourceImage[x-1,y-1])+(sobelx[0][1]*sourceImage[x,y-1])+(sobelx[0][2]*sourceImage[x+1,y-1])+(sobelx[1][0]*sourceImage[x-1,y])+(sobelx[1][1]*sourceImage[x,y])+(sobelx[1][2]*sourceImage[x+1,y])+(sobelx[2][0]*sourceImage[x-1,y+1])+(sobelx[2][1]*sourceImage[x,y+1])+(sobelx[2][2]*sourceImage[x+1,y+1])

        #Compute Gy
        Gy = (sobely[0][0]*sourceImage[x-1,y-1])+(sobely[0][1]*sourceImage[x,y-1])+(sobely[0][2]*sourceImage[x+1,y-1])+(sobely[1][0]*sourceImage[x-1,y])+(sobely[1][1]*sourceImage[x,y])+(sobely[1][2]*sourceImage[x+1,y])+(sobely[2][0]*sourceImage[x-1,y+1])+(sobely[2][1]*sourceImage[x,y+1])+(sobely[2][2]*sourceImage[x+1,y+1])

        #Intermediate Results
        val1 = Gx*Gx
        val2 = Gy*Gy

        #Apply formula sqrt(GxSquare + GySquare)
        val3 = m.sqrt(val1+val2)
        #print val3

        #Check for value < 0 and > 255
        if(val3 < 0):
            val3 = 0
        if(val3 > 255):
            val3 = 255

        #Store Computed Value    
        destImage[x][y] = 255-int(val3)

print 'time to compute  - in seconds'
stop = timeit.default_timer()
print stop-start 

#Display Result        
plt.imshow(destImage, cmap = 'gray')
plt.title('Sobel Custom Code Output ')
plt.show()

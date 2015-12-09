#       About - Convolution Operation - Apply filter m x n on a Input Image
#       Updated             07/10/2015
#       Load the input image
#       Determine the kernel size, identify kernel neighbourhood points to compute dot product
#       Compute the convolution (dot product operation)
#       Return Convoluted Image

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Load Input Image
sourceImage = cv2.imread('marilyn.bmp')
sourceImage = cv2.cvtColor(sourceImage,cv2.COLOR_BGR2GRAY)

#Initialize output Image
resultimage = sourceImage[0:sourceImage.shape[0],0:sourceImage.shape[1]]

#Compute convolution function
def computeConvolution(inputimage, filtervalues):
        
        #input image width and height
        width = inputimage.shape[0]
        height = inputimage.shape[1]

        #kernel width and height
        width1 = filtervalues.shape[0]
        height1 = filtervalues.shape[1]

        midwidth = (width1)/2
        midheight = (height1)/2

        #Create Output Image
        resultimage = inputimage[0:width,0:height]

        #Loop thru width of Input Image
        for x in range(0,width):

                #Loop thru height of Input Image
                for y in range(0,height):

                                #Initialize computed value to zero
                                resultimage[x][y] = 0
                                sum = 0.0
                                #Loop through width of filter
                                for u in range(0,width1):

                                                #Loop through height of filter
                                                for v in range(0,height1):

                                                         #Identify Neighbour pixel points to Pick for Applying filter
                                                         kx = x+u-midwidth
                                                         ky = y+v-midheight
                                                         #print kx,ky

                                                #Zero, width, height restrictions check
                                                if (kx >= 0 and kx < width and ky >= 0 and ky < height):

                                                        #Computed dot product sum of image and filter
                                                        sum += inputimage[kx][ky]*filtervalues[u][v];
                                                        
                                #print sum            
                                resultimage[x][y] = sum
        print 'Convolution completed'
        resultimage = np.abs(resultimage)        
        return resultimage

#filter1 - Sharpen Filter
print 'Run1 - Sharpen Filter 3x3 filter'
filtervalues = np.array([[0,1,0],[1,-8,1],[0,1,0]],np.double)

#compute convolution
resultimage = computeConvolution(sourceImage,filtervalues)

plt.subplot(121)
plt.imshow(resultimage, cmap = 'gray')
plt.title('Run1 - Sharpen Filter - 3x3 filter')

print 'Run2 - Smoothen Filter 4x4 filter'
#filter2 Smoothen Filter - Guass 1/9 smoothen values
filtervalues1 = np.array([[.111,.111,.111,.111],[.111,.111,.111,.111],[.111,.111,.111,.111],[.111,.111,.111,.111]],np.double)

#compute convolution
resultimage1 = computeConvolution(sourceImage,filtervalues1)

plt.subplot(122)
plt.imshow(resultimage1, cmap = 'gray')
plt.title('Guass 1/9 smoothen values - 4x4 filter ')
plt.show()

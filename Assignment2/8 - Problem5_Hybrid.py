#       Load two Images I1 and I2, Apply Guass Blur one one image I1
#       Apply Image Sharpening on Image I2
#       Merge both Images with 40-60 ratio of both to produce hybrid image
import cv2
import numpy as np
import math as m

#Load Image
sourceImage1 = cv2.imread('cat.bmp')
sourceImage1 = cv2.cvtColor(sourceImage1,cv2.COLOR_BGR2GRAY)

sourceImage2 = cv2.imread('dog.bmp')
sourceImage2 = cv2.cvtColor(sourceImage2,cv2.COLOR_BGR2GRAY)

cv2.imshow('cat',sourceImage1)

cv2.imshow('dog',sourceImage2)

#Image Blur Kernel 3 X 3 Kernel
Gauss = np.array([ [0.1111,0.1111,0.1111],[0.1111,0.1111,0.1111],[0.1111,0.1111,0.1111]],np.double)

#Image Sharpen Kernel
sharpenKernel = np.array([ [0,0.2,0],[0.2,-1,0.2],[0,0.2,0]],np.double)

#print Gauss
#print sharpenKernel

width1 = sourceImage1.shape[0]
height1 = sourceImage1.shape[1]

width2 = sourceImage2.shape[0]
height2 = sourceImage2.shape[1]

destGaussImage = sourceImage1[0:width1,0:height1]
destImage = sourceImage2[0:width2,0:height2]

#Compute value for each row
#Sum them up
for y in range(1,height1-1):
    for x in range(1,width1-1):
        destGaussImage[x][y] = 0
        #print destGaussImage[x][y]
        row1Val = 0
        row2Val = 0
        row3Val = 0
        
        #Multiple by 0.11,0.11,0.11
        row1Val = (Gauss[0][0]*sourceImage1[x-1,y-1])+(Gauss[0][1]*sourceImage1[x-1,y])+(Gauss[0][2]*sourceImage1[x-1,y+1])

        #Multiple by 0.11,0.11,0.11
        row2Val = (Gauss[1][0]*sourceImage1[x,y-1])+(Gauss[1][1]*sourceImage1[x,y])+(Gauss[1][2]*sourceImage1[x,y+1])
    
        #Multiple by 0.11,0.11,0.11
        row3Val = (Gauss[2][0]*sourceImage1[x+1,y-1])+(Gauss[2][1]*sourceImage1[x+1,y])+(Gauss[2][2]*sourceImage1[x+1,y+1])

        resultValue = row1Val+row2Val+row3Val
        #print resultValue
        #print destGaussImage[x][y]
        destGaussImage[x][y] = resultValue

cv2.imshow('cat smoothened',destGaussImage)

for y in range(1,height2-1):
    for x in range(1,width2-1):
        destImage[x][y] = 0
        #print destImage[x][y]
        row1Val = 0
        row2Val = 0
        row3Val = 0
        
        #Multiple by [0,0.2,0]
        row1Val = (sharpenKernel[0][0]*sourceImage2[x-1,y-1])+(sharpenKernel[0][1]*sourceImage2[x-1,y])+(sharpenKernel[0][2]*sourceImage2[x-1,y+1])

        #Multiple by [0.2,-1,0.2]
        row2Val = (sharpenKernel[1][0]*sourceImage2[x,y-1])+(sharpenKernel[1][1]*sourceImage2[x,y])+(sharpenKernel[1][2]*sourceImage2[x,y+1])
    
        #Multiple by [0,0.2,0]
        row3Val = (sharpenKernel[2][0]*sourceImage2[x+1,y-1])+(sharpenKernel[2][1]*sourceImage2[x+1,y])+(sharpenKernel[2][2]*sourceImage2[x+1,y+1])

        resultValue = row1Val+row2Val+row3Val

        #print resultValue
        destImage[x][y] = resultValue

cv2.imshow('Dog sharpened',destImage)
dst = cv2.addWeighted(destGaussImage,0.4,destImage,0.6,0)

cv2.imshow('Hybrid image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

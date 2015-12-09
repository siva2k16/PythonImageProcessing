#       About - Compute Harris Corner Detection
#       Updated             09/12/2015

import cv2
import numpy as np
import math as m
import timeit
from scipy import *
from scipy import signal
from scipy.ndimage import filters
from pylab import *
from scipy import ndimage

def ComputeHarrisCorner(sourceImage, kconstant, mindistance, threshold):
    #start timer
    start = timeit.default_timer()
    sourceImage = cv2.cvtColor(sourceImage,cv2.COLOR_BGR2GRAY)

    destImageGx =  zeros(sourceImage.shape)
    destImageGy =  zeros(sourceImage.shape)

    destImageGx = cv2.Sobel(sourceImage, cv2.CV_32F, 1, 0)
    destImageGy = cv2.Sobel(sourceImage, cv2.CV_32F, 0, 1)

    Ixx = zeros(sourceImage.shape)
    Iyy = zeros(sourceImage.shape)
    Ixy = zeros(sourceImage.shape)

    Ixx = destImageGx*destImageGx
    Iyy = destImageGy*destImageGy
    Ixy = destImageGx*destImageGy

    #Convolve Ixx, Iyy and IxIy with Gaussians to obtain Wxx, Wyy, Wxy
    Wxx = filters.gaussian_filter(Ixx*Ixx, 3)
    Wyy = filters.gaussian_filter(Iyy*Iyy, 3)
    Wxy = filters.gaussian_filter(Ixy*Ixy, 3)

    cornerness = zeros(sourceImage.shape)
    cornerness = np.float32(cornerness)

    trace = zeros(sourceImage.shape)
    determinant = zeros(sourceImage.shape)

    trace = Wxx+Wyy
    determinant = (Wxx*Wyy)-(Wxy*Wxy)

    #(k – empirical constant, k = 0.04-0.06)
    cornerresponse =determinant - (kconstant*trace*trace)
    print cornerresponse
    
    windowsize = zeros(cornerresponse.shape)
    windowsize[mindistance:-mindistance,mindistance:-mindistance] = 1
    selectedpoints = []
    coords = []
    pick_values = []

    #Flat Array M=from MXN of cornerresponse
    corner_threshold = max(cornerresponse.ravel())*threshold
    cornerresponsethreshold = (cornerresponse>corner_threshold)*1
    pickcoordinates = cornerresponsethreshold.nonzero()

    coords = [(pickcoordinates[0][c],pickcoordinates[1][c]) for c in range(len(pickcoordinates[0]))]
    pick_values = [cornerresponse[c[0]][c[1]] for c in coords]

    noofelements = argsort(pick_values)
    for i in noofelements:
        if windowsize[coords[i][0]][coords[i][1]] == 1:
            selectedpoints.append(coords[i])
            windowsize[(coords[i][0]-mindistance):(coords[i][0]+mindistance),(coords[i][1]-mindistance):(coords[i][1]+mindistance)] = 0
    figure()
    gray()
    imshow(sourceImage)
    plot([val[1] for val in selectedpoints],[val[0] for val in selectedpoints],'.')
    axis('off')
    show()
    stop = timeit.default_timer()
    print 'time to run'
    print stop-start
    cv2.waitKey(0)

#Test with different images
kconstant = 0.05
mindistance = 1
threshold = 0.3
sourceImage = cv2.imread('grid1.jpg')
ComputeHarrisCorner(sourceImage, kconstant, mindistance, threshold)

kconstant = 0.05
mindistance = 1
threshold = 0.4
sourceImage = cv2.imread('grid2.jpg')
ComputeHarrisCorner(sourceImage, kconstant, mindistance, threshold)
    
kconstant = 0.05
mindistance = 1
threshold = 0.01
sourceImage = cv2.imread('grid_rotated.jpg')
ComputeHarrisCorner(sourceImage, kconstant, mindistance, threshold)

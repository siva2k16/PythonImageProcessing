#Problem 5. Exercise #1. Generate Negative Image
#	30/08/2015		Draft Version
#Approaches using inbuilt function invert, pixel computation

import PIL.ImageOps    
import cv2
import numpy as np
from PIL import Image


#Approach #1 - using pixel manipulation functions
def invertImageFunctionbyPixelManipulation():
    #Zero will load grey scale
    sourceImage = cv2.imread('einstein.jpg',0)
    sourceImage = 255-sourceImage
    cv2.imshow('Negative of Grey Image',sourceImage)
    cv2.waitKey(0)

#Approach #2 - using inbuilt functions
def invertImageFunction():
    #Load Image
    image = Image.open('einstein.jpg')

    #Invert Image
    inverted_image = PIL.ImageOps.invert(image)

    #Save Inverted Image
    inverted_image.save('negativeImage.jpg')

    #Load Image
    InvertedImage = cv2.imread('negativeImage.jpg')

    #Display Image
    cv2.imshow('NegativeExample1 of Color Image',InvertedImage)
    cv2.waitKey(0)

#Invoke Function
invertImageFunctionbyPixelManipulation()
invertImageFunction()

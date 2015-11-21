#5. Add or subtract a random value between [0,255] to every pixel in a grayscale image, then clip the resulting image to have a minimum value of 0 and a maximum value of 255. 
#	30/08/2015		Draft Version

import cv2
import numpy as np
from matplotlib import pyplot as plt
from random import randint

#RandomValue on Image Example
def RandomValueAppliedExample():
    sourceImage = cv2.imread('einstein.jpg',0)

    #generate a random number and add it to image
    randomnumber = randint(1,255)
    print randomnumber

    newimage = randomnumber+sourceImage
    
    if(newimage.any() > 255):
        newimage[newimage] = 255

    cv2.imshow('Result image with Noise',newimage)
    cv2.waitKey(0)

#Invoke Function
RandomValueAppliedExample()



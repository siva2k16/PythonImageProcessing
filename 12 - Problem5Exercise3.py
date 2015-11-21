#3. Swap the red and green color channels of the input color image. 
#	30/08/2015		Draft Version

import cv2
#Swap R and G Channels using inbuilt functions
def swapRandGChannelsInbuiltFunction():
    sourceImage = cv2.imread('dreamflower.jpg')
    #Split into Channels
    blue,green,red = cv2.split(sourceImage)
    AvgdestImage = sourceImage[0:sourceImage.shape[0],0:sourceImage.shape[1]]
    #Merge with Swapped Channels
    AvgdestImage = cv2.merge((blue,red,green))
    cv2.imshow('R and G swapped image using Inbuilt functions',AvgdestImage)
    cv2.waitKey(0)

#Invoke function
swapRandGChannelsInbuiltFunction()




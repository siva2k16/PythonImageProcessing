#5. Generate a new image, which is the same as A, but with As mean intensity value subtracted from each pixel. 
#		30/08/2015		Draft Version
import cv2
import Image
import numpy as np

sourceImage = cv2.imread('einstein.jpg')

#Compute Mean of Image
frame_mean = np.sum(sourceImage) / float(sourceImage.shape[0] * sourceImage.shape[1] * sourceImage.shape[2])
print frame_mean

#Subtract mean from every pixel
sourceImage = sourceImage-frame_mean

sourceImage[sourceImage < 0] = 0

print sourceImage

cv2.imshow('Mean Intensity Manipulated Result2',sourceImage)
cv2.waitKey(0)

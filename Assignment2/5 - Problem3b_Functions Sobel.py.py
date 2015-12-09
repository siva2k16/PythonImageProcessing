#       Sobel using inbuilt functions
import cv2
import numpy as np
from matplotlib import pyplot as plt
import timeit

img = cv2.imread('u2cuba.jpg',0)

#start timer
start = timeit.default_timer()

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

print 'Sobel - time to compute - Inbuilt function'
stop = timeit.default_timer()
print stop-start 

plt.subplot(2,2,1)
plt.imshow(img,cmap = 'gray')
plt.title('Original Picture'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X Applied'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y Applied'), plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)

#       About - Fast Fourier computation, phase, magnitude and image reconstruction
#       Updated             11/10/2015
#       Load the input image
#       Function for Phase computation - computePhase
#       Function for Magnitude computation - computeMagnitude

import cv2
import Image
import numpy as np
from matplotlib import pyplot as plt

#function for phase computation
def computePhase(img):
    #Returns 2D discrete FT of Image
    #fft2 returns complex array
    f = np.fft.fft2(img)

    #Shift the zero frequency to the centre of array
    #These shift the image so that the low frequencies are at the center
    fshift = np.fft.fftshift(f)

    #phase of image
    phase = np.angle(fshift)
    return phase

#function for magnitude computation
def computeMagnitude(img):
    f = np.fft.fft2(img)

    #Shift the zero frequency to the centre of array
    #These shift the image so that the low frequencies are at the center
    fshift = np.fft.fftshift(f)

    #Compute Magnitude of change
    magnitude_spectrum = 20*np.log(np.abs(fshift))

    return magnitude_spectrum

#Step1 - compute magnitude and intensity of mandrill
mandrill = cv2.imread('mandrill.tif',0)
phaseimg = computePhase(mandrill)
magnitude_mandrill = computeMagnitude(mandrill)

plt.subplot(2,2,1)
plt.imshow(phaseimg,cmap = 'gray')
plt.title('Phase mandrill'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2)
plt.imshow(magnitude_mandrill,cmap = 'gray')
plt.title('Magnitude mandrill'), plt.xticks([]), plt.yticks([])

#Step2 - compute magnitude and intensity of clown
clown= cv2.imread('clown.tif',0)
phaseimg1 = computePhase(clown)
magnitude_clown = computeMagnitude(clown)

plt.subplot(2,2,3)
plt.imshow(phaseimg1,cmap = 'gray')
plt.title('Phase clown'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(magnitude_clown,cmap = 'gray')
plt.title('Magnitude clown'), plt.xticks([]), plt.yticks([])
plt.show()

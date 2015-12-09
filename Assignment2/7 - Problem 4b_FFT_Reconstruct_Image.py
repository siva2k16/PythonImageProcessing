#       About - Fast Fourier computation, and image reconstruction using Phase & Magnitude Swapped
#       Updated             11/10/2015
#       Load the input image
#       Function to swap phase and magnitude between two images - computeNewImage

import cv2
import Image
import numpy as np
from matplotlib import pyplot as plt

#function for image reconstruction by swapping phase and magnitude of two different images
def computeNewImage(img, img1):
    #Returns 2D discrete FT of Image
    fourier_img1 = np.fft.fft2(img)

    #These shift the image so that the low frequencies are at the center
    fshift_img1 = np.fft.fftshift(fourier_img1)

    #Magnitude of Image1
    magnitude_img1  = np.abs(fshift_img1)

    #Phase of Image1
    phase_img1 = np.angle(fshift_img1)

    #Returns 2D discrete FT of Image
    fourier_img2 = np.fft.fft2(img1)
    fshift_img2 = np.fft.fftshift(fourier_img2)

    #Magnitude of Image2
    magnitude_img2  = np.abs(fshift_img2)

    #Phase of Image1
    phase_img2 = np.angle(fshift_img2)

    #compute Inverse between two images - Magnitude of Image1 + Phase of Image2
    newswappedreal =	magnitude_img1*np.cos(phase_img2)	
    newwappedim  =	magnitude_img1*np.sin(phase_img2)	

    #create the new image with magnitude and phase swapped
    fnewimage = newswappedreal +1j*newwappedim

    f_ishift = np.fft.ifftshift(fnewimage)

    #inverse fft
    newimagereturned = np.fft.ifft2(f_ishift)	
    newimagereturned = np.abs(newimagereturned)

    #return reconstructed image
    return newimagereturned

mandrill = cv2.imread('mandrill.tif',0)
clown= cv2.imread('clown.tif',0)

#param1 - Magnitude
#param1 - Phase

print ' Magnitude of mandrill + Phase of clown'
newimagemandrillPhase = computeNewImage(mandrill,clown)

print ' Magnitude of clown + Phase of mandrill'
newimageclownPhase = computeNewImage(clown,mandrill)

plt.subplot(121)
plt.imshow(newimagemandrillPhase, cmap = 'gray')
plt.title('Phase of clown + Magnitude of mandrill'), plt.xticks([]), plt.yticks([])

plt.subplot(122)
plt.imshow(newimageclownPhase, cmap = 'gray')
plt.title('Phase of mandrill + Magnitude of clown'), plt.xticks([]), plt.yticks([])

plt.show()

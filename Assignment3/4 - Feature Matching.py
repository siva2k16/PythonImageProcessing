#       About - Feature matching using SIFT
#       Updated             09/12/2015

import numpy as np
import cv2
from matplotlib import pyplot as plt
from find_obj import filter_matches,explore_match

#Finding K Nearest Neighbours
def knearestneighbours(img1, des1, img2, des2, kp1, kp2):
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2, k=2)
    return matches

#Aply Ratio Test
def applyRatioTest(matches):
    good = []
    for m,n in matches:
        if m.distance < 0.6*n.distance:
            good.append([m])
    return good

#Plot Matches
def PlotMatches(sourceImage, kp1, rotatedImage, kp2, matches):
    p1, p2, kp_pairs = filter_matches(kp1, kp2, matches)
    explore_match('K Nearest Neighbours', sourceImage,rotatedImage,kp_pairs)
    cv2.waitKey()
    cv2.destroyAllWindows()

#compute sift
def ComputeSift(img1, img2):
    #read input and rotated images
    sift = cv2.SIFT()
    kp1, des1 = sift.detectAndCompute(sourceImage,None)
    kp2, des2 = sift.detectAndCompute(rotatedImage,None)
    return kp1, des1, kp2, des2 

sourceImage = cv2.imread('taj1.jpg',0)   
rotatedImage = cv2.imread('taj2.jpg',0) 
kp1, des1, kp2, des2 = ComputeSift(sourceImage,rotatedImage)
#K Nearest Neughbours
matches = knearestneighbours(sourceImage, des1, rotatedImage, des2, kp1, kp2)
# Apply ratio test
ratiotest = applyRatioTest(matches)
#Plot Matches
PlotMatches(sourceImage, kp1, rotatedImage, kp2, matches)

sourceImage = cv2.imread('makingcomics1.png',0)   
rotatedImage = cv2.imread('makingcomics2.png',0) 
kp1, des1, kp2, des2 = ComputeSift(sourceImage,rotatedImage)
#K Nearest Neughbours
matches = knearestneighbours(sourceImage, des1, rotatedImage, des2, kp1, kp2)
# Apply ratio test
ratiotest = applyRatioTest(matches)
#Plot Matches
PlotMatches(sourceImage, kp1, rotatedImage, kp2, matches)

sourceImage = cv2.imread('notredame1.jpg',0)   
rotatedImage = cv2.imread('notredame2.jpg',0) 
kp1, des1, kp2, des2 = ComputeSift(sourceImage,rotatedImage)
#K Nearest Neughbours
matches = knearestneighbours(sourceImage, des1, rotatedImage, des2, kp1, kp2)
# Apply ratio test
ratiotest = applyRatioTest(matches)
#Plot Matches
PlotMatches(sourceImage, kp1, rotatedImage, kp2, matches)


#4. Average the input image with its mirror image. 
#	30/08/2015		Draft Version

import cv2

#Define and implement mirror function
def mirrorImageExample():
    sourceImage=cv2.imread('einstein.jpg')
    destImage=sourceImage.copy()
    destImage=cv2.flip(sourceImage,1)

    #Display Mirrored Image
    #cv2.imshow('mirrored image',destImage)

    #Saved in Local Scripts Directory
    cv2.imwrite('mirrored.jpg',destImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Average of Mirror and Original Image
def avgMirrorImageExampleInbuiltFunctionExample():
    img1 = cv2.imread('einstein.jpg')
    img2 = cv2.imread('mirrored.jpg')
    dst = cv2.addWeighted(img1,0.5,img2,0.5,0)
    cv2.imshow('average mixed image',dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Invoke Mirror function 
mirrorImageExample()
#Average with Original and Mirrored Image
avgMirrorImageExampleInbuiltFunctionExample()

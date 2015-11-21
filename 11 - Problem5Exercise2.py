#Code to mirror image from left to right
#	30/08/2015		Draft Version
#Using Flip function and pixel level manipulation

import cv2

#Approach #1
#Define and implement mirror function
def mirrorImageInbuiltFuncExample():
    sourceImage=cv2.imread('einstein.jpg')
    flipImage=sourceImage.copy()
    flipImage=cv2.flip(sourceImage,1)
    cv2.imshow("Flipped image", flipImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Approach #2
#Define and implement mirror function
def mirrorImageExample():
    #Load Image
    sourceImage = cv2.imread('einstein.jpg')
    print sourceImage

    cv2.imshow('Original Image',sourceImage)

    #Identify No of Rows
    row = sourceImage.shape[0]
    #Identify No of Columns
    column = sourceImage.shape[1]

    #Create Destination Image of Same Size
    destImage = sourceImage[0:row,0:column]

    #Midpoint
    ylimit = column/2

    #Exchage (0,n-1),(1,n-2)...until midpoint

    #Parse through every element in image, compute and Display
    for x in range(0,sourceImage.shape[0]):
        for y in range(0,ylimit):
                   val = column-y-1

                   #End Pixel
                   sourceValPx = sourceImage[x][val][0]
                   sourceValPy = sourceImage[x][val][1]
                   sourceValPz = sourceImage[x][val][2]

                   #Beginning Pixel
                   destValPx = sourceImage[x][y][0]
                   destValPy = sourceImage[x][y][1]
                   destValPz = sourceImage[x][y][2]

                   #Assign them in new Image
                   destImage.itemset((x,y,0),sourceValPx)
                   destImage.itemset((x,y,1),sourceValPy)
                   destImage.itemset((x,y,2),sourceValPz)

                   #Assign them in new Image
                   destImage.itemset((x,val,0),destValPx)
                   destImage.itemset((x,val,1),destValPy)
                   destImage.itemset((x,val,2),destValPz)

    #Display Mirrored Image
    cv2.imshow('pixel mirrored image',destImage)

    #Saved in Local Scripts Directory
    cv2.imwrite('mirrored.jpg',destImage)
    cv2.waitKey(0)

#Invoke Mirror function 
mirrorImageInbuiltFuncExample()
mirrorImageExample()


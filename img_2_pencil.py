import numpy as np
import cv2 as cv
# pip install opencv-python

def convert(image):
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)     #coversion to gray scale image
    inv_gray=255-gray                    #inverting the gray image by subtracting from 255 (RGB ranges from 0 to 255)
    blur=cv.GaussianBlur(inv_gray,(21,21),0)      #blur the inverted gray image
    inv_blur=255-blur                             #inverting the blurred image 
    pencil=cv.divide(gray,inv_blur,scale=256.0)   #diving the gray and inverted blurr image for output pencil sketch
    return pencil

img=str(input("Enter the Image location: "))      # D:\manor\Pictures\Saved Pictures\dog.jpg

img=cv.imread(img)                                #Read the image from location
image=np.copy(img)                                #copy the object image for defined function using numpy.copy
ps_image=convert(image)

cv.imshow('Original Image',image)
cv.imshow('Pencil Sketch',ps_image)
cv.waitKey(0)
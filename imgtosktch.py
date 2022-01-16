#import the opencv library , if you don't have, command to install it is : pip install opencv-python
import cv2

img=str(input("Give Image Location: "))                # D:\manor\Pictures\Saved Pictures\naruto.jpg
img= cv2.imread(img)                                   #Read the image from location 
gray_img =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        #coversion to gray scale image 
inv_gray_img = 255 - gray_img                          #inverting the gray image by subtracting from 255
blurr_img = cv2.GaussianBlur(inv_gray_img, (21,21) ,0) #blur the inverted gray image
inv_blurr_img = 255 - blurr_img                        #inverting the blurred image

# diving the gray and inverted blurr image for output pencil sketch
pencilsketch_img = cv2.divide(gray_img, inv_blurr_img, scale=256.0) 

cv2.imshow('Original image',img)
# cv2.imshow('Gray image',gray_img)
# cv2.imshow('Inverted Gray image',inv_gray_img)
# cv2.imshow('Blurred image',blurr_img)
# cv2.imshow('Inverted blurred image',inv_blurr_img)
cv2.imshow('Pencil sketch image',pencilsketch_img)
cv2.waitKey(0)         #{ waitkey() allows to display for given milisecond, 
                       #  and 0 argument allows to hold window till any key press  }

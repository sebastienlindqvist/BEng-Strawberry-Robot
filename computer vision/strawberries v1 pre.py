import cv2
import numpy as np
import matplotlib.pyplot as plt
import random as rng
from PIL import Image


def Main():
    #receiving the image
    image=cv2.imread('test_image.jpg')
    image_copy =np.copy(image)

    #all the functions
    image_copy=red(image_copy)
    #image_copy=canny(image_copy)
    #image_copy=contours(image,image_copy)
    #image_copy=real(image,image_copy)
    #resizing and showing image
    image_copy=cv2.resize(image_copy,(2000,1000))
    cv2.imshow('gray scale',image_copy)
    cv2.waitKey(0)


def save(image,a,b,c,d):
    cropped=image[a:c,b:d]
    cv2.imwrite("cropped.jpg",cropped)
    return 0
def real(image,image_copy):
    image = cv2.addWeighted(image, 1, image_copy, 1, 0.0)
    return image

def red(image):
    #this is to find the colour red using HSV range
    image=cv2.GaussianBlur(image, (101,101),0)
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    #lower red
    #lower_red=np.array([0,120,0])#hue saturation and value
    #upper_red=np.array([10,255,255])
    #mask1=cv2.inRange(hsv, lower_red, upper_red)
    #range for upper range
    #lower_red = np.array([170,120,100])
    #upper_red = np.array([180,255,255])
    #mask2 = cv2.inRange(hsv,lower_red,upper_red)
    #Over lapping masks
    #mask1 = mask1+mask2
    #over laying 
    #red = cv2.bitwise_and(image, image, mask= mask1)
    return hsv


def contours(image_original,image):
    IMGcontours, hierarchy = cv2.findContours(image,
            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#on raspberry pi it needs _,   ,_
    cv2.drawContours(image, IMGcontours, -1, (0, 255, 0), 3)
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (50, 50) 
    # Approximate contours to polygons + get bounding rects and circles
    contours_poly = [None]*len(IMGcontours)
    boundRect = [None]*len(IMGcontours)
    centers = [None]*len(IMGcontours)
    radius = [None]*len(IMGcontours)
    for i, c in enumerate(IMGcontours):
        contours_poly[i] = cv2.approxPolyDP(c, 3, True)
        boundRect[i] = cv2.boundingRect(contours_poly[i])
        centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])
    drawing = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    # Draw polygonal contour + circles
    color=(256,256,256)
    for i in range(len(IMGcontours)):
        if(int(boundRect[i][3])>=250):#>=250#10
            cv2.rectangle(drawing, (int(boundRect[i][0])-10, int(boundRect[i][1])-10),
                (int(boundRect[i][0]+boundRect[i][2])+10, int(boundRect[i][1]+boundRect[i][3])+10), color, 10)
            cv2.drawContours(drawing, contours_poly, i, color)
            cv2.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 10)
            cv2.circle(drawing, (int(centers[i][0]), int(centers[i][1])), 1, color, 10)
            save(image_original,int(boundRect[i][1])-10,int(boundRect[i][0])-10,
                 int(boundRect[i][1]+boundRect[i][3])+10,int(boundRect[i][0]+boundRect[i][2])+10)
    return drawing





def blur(image):
    blur=cv2.GaussianBlur(image, (5,5),0)
    return blur

def gray(image): #converts image to gray scale
    gray=cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return gray

def canny(image): #This is to find edges in an image
    image=gray(image)
    image=blur(image)
    image=cv2.Canny(image,10,100)
    return image


Main()
    


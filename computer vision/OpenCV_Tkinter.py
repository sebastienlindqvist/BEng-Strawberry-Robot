from tkinter import *
from PIL import ImageTk, Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import random as rng
import os.path
from os import path




def tkGUI():
    global window
    window=Tk()
    window.title('OpenCV GUI')
    #Declare Variables
    Img2Check()
    #Declaring Canvas
    global canv2
    canv,canv2=DeclareCanvas(window)
    #Images
    image=cv2.imread('test_image.jpg')
    image2=cv2.imread('test_image2.jpg')
    img =FormatImageCanvas(image)
    img2=FormatImageCanvas(image2)
    Canv(img,img2,canv,canv2)
    #Declaring Labels
    label=Label(window, text='').grid(row=0,column=2)
    #Declaring Buttons
    btn1=Button(window,text="previous").grid(row=0,column=0)
    btn2=Button(window,text="next").grid(row=0,column=1)
    
    btn4=Button(window,text="Red",command=red(image)).grid(row=0,column=4)
    btn3=Button(window,text="Gray",command=gray(image)).grid(row=0,column=3)
    btn5=Button(window,text="Green").grid(row=0,column=5)
    btn6=Button(window,text="Canny").grid(row=0,column=6)
    window.mainloop()

def Img2Check():
    if path.exists("test_image2.jpg")==False:
        image=cv2.imread('test_image.jpg')
        cv2.imwrite('test_image2.jpg',image)

def Canv(img,img2,canv,canv2):
    canv.create_image((224,168),image=img)
    canv2.create_image((224,168),image=img2)


def DeclareCanvas(window):
    canv = Canvas(window, width=448, height=336, bg='white')
    canv2 = Canvas(window, width=448, height=336, bg='white')
    canv.grid(row=1, column=0, columnspan=2)
    canv2.grid(row=1, column=3, columnspan=4)
    return canv,canv2

def FormatImageCanvas(img):
    #Note: this line is need down below or else blue and red switch. could be useful
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img,(448,336))
    img=Image.fromarray(img)
    img=ImageTk.PhotoImage(img)
    return img

def Update():
    window.configure()
    print('hello')



def red(image):
    #this is to find the colour red using HSV range
    image=cv2.GaussianBlur(image, (21,21),0)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #lower red
    lower_red=np.array([0,120,0])
    upper_red=np.array([10,255,255])
    mask1=cv2.inRange(hsv, lower_red, upper_red)
    #range for upper range
    lower_red = np.array([170,120,0])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
    #Over lapping masks
    mask1 = mask1+mask2
    #over laying 
    red = cv2.bitwise_and(image, image, mask= mask1)

    cv2.imwrite('test_image2.jpg',red)
    Update()
    return red

def blur(image):
    blur=cv2.GaussianBlur(image, (5,5),0)
    return blur

def gray(image): #converts image to gray scale
    gray=cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cv2.imwrite('test_image2.jpg',gray)
    Update()
    return gray

def canny(image): #This is to find edges in an image
    image=gray(image)
    image=blur(image)
    image=cv2.Canny(image,10,100)
    return image

tkGUI()

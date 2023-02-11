import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from strawberries import red
#from strawberries import contours
from strawberries import gray
import math






def Main():
    image=cv2.imread('cropped.jpg')
    im=Image.open('cropped.jpg')
    image_copy =np.copy(image)

    image_copy=red(image_copy)
    image_copy=gray(image_copy)

    #----------------------------------------
    #     Assinging Variables
    #----------------------------------------------
    width, height = im.size
    centre=np.array([[int(width/2)],[int(height/2)]])
    top=np.array([[int(width/2)],[int((height/2)-100)]])
    bottom=np.array([[int(width/2)],[int((height/2)+100)]])
    x=np.array([[int(width/2)],[0]])
    x2=np.array([[int(width/2)],[1000]])
    
    
    #cv2.circle(image_copy,(2686,2325),2,(255,255,0), 10)


    centreX,image_copy=Contours(image_copy)
    centreX=np.array(centreX)
    centre=centreX.reshape(2,1)
    
    x=np.array([[centre[0][0]],[0]])
    x2=np.array([[centre[0][0]],[1000]])
    print(centre[1][0])

    DistanceAndAngles(centre,image_copy)
    
    #------------------------------------------------------------------------------------------------
    #
    #-------------------------------------------------------------------------------------------------
    if (False):
        for a in range(1):
            #-----------------------------------------------
            # Matrixes
            #-----------------------------------------------
            #a=10*a
            matrix=np.array([[math.cos(math.radians(a)),-math.sin(math.radians(a))],
                [math.sin(math.radians(a)),math.cos(math.radians(a))]])
            matrix2=np.array([[math.cos(math.radians(a+90)),-math.sin(math.radians(a+90))],
                [math.sin(math.radians(a+90)),math.cos(math.radians(a+90))]])
            #-----------------------------------------------
            # Updating
            #-----------------------------------------------
            x=centreX+matrix.dot(x-centreX)
            x2=centreX+matrix.dot(x2-centreX)
            #
            #x5=centre+matrix2.dot(x-centre)
            #x6=centre+matrix2.dot(x2-centre)
            for i in range(10):
                x=np.array([[int(centre[0][0])],[int(centre[1][0])-i*25]])
                x2=np.array([[int(centre[0][0])],[int(centre[1][0])+i*25]])
                x=centre+matrix.dot(x-centre)
                x2=centre+matrix.dot(x2-centre)
                cv2.circle(image_copy,tuple(x),2,(255,255,0), 1)
                cv2.circle(image_copy,tuple(x2),2,(255,255,0), 1)
                for c in range(20):
                    x3=np.array([[int(centre[0][0])+c*30],[int(centre[1][0])-i*100]])
                    x4=np.array([[int(centre[0][0])-c*30],[int(centre[1][0])-i*100]])
                    x5=np.array([[int(centre[0][0])-c*30],[int(centre[1][0])+i*100]])
                    x6=np.array([[int(centre[0][0])+c*30],[int(centre[1][0])+i*100]])
                    #x=np.rint(centre+matrix.dot(x-centre))
                    #x2=centre+matrix.dot(x2-centre)
                    x3=np.rint(centre+matrix.dot(x3-centre))
                    x4=centre+matrix.dot(x4-centre)
                    x5=centre+matrix.dot(x5-centre)
                    x6=centre+matrix.dot(x6-centre)
                    #for i, c in enumerate(IMGcontours):
                        #z=IMGcontours[b].index(int(x3))
                    for b in range(len(IMGcontours)):
                        for n in range(len(IMGcontours[b])):
                            z=np.where(IMGcontours[b][n-1][0]==102)
                            if(z[0].size != 0):
                            #l=(IMGcontours[b][n-1][0])
                                B=b
                                N=n-1
                                #print(IMGcontours[B][N][0])

                    if((x3[0][0]>=0 and x3[1][0]>=0)       ):
                        #print(x3)
                        cv2.circle(image_copy,tuple(x3),2,(255,0,0), 1)
                    if(x4[0][0]>=0 and x4[1][0]>=0):
                        cv2.circle(image_copy,tuple(x4),2,(255,0,0), 1)
                    if(x5[0][0]>=0 and x5[1][0]>=0):
                        cv2.circle(image_copy,tuple(x5),2,(255,0,0), 1)
                    if(x6[0][0]>=0 and x6[1][0]>=0):
                        cv2.circle(image_copy,tuple(x6),2,(255,0,0), 1)
        #print(x3)
        #------------------------------------------------------------------------------------------------
        #
        #-------------------------------------------------------------------------------------------------
        top=centre+matrix.dot(top-centre)
        bottom=centre+matrix.dot(bottom-centre)
        
        topx5=top+matrix2.dot(x-centre)
        topx6=top+matrix2.dot(x2-centre)
        bottomx5=bottom+matrix2.dot(x-centre)
        bottomx6=bottom+matrix2.dot(x2-centre)
        #---------------------------------------------
        # change in y over change in x
        #---------------------------------------------
        #gradient=(x4[1,0]-x3[1,0])/(x4[0,0]-x3[0,0])


        #---------------------------------------------
        # printing
        #---------------------------------------------

        image_copy=cv2.line(image_copy,tuple(x3),tuple(x4),(0,255,0),3)
        image_copy=cv2.line(image_copy,tuple(x5),tuple(x6),(0,0,255),3)
        image_copy=cv2.line(image_copy,tuple(topx5),tuple(topx6),(0,0,255),3)
        image_copy=cv2.line(image_copy,tuple(bottomx5),tuple(bottomx6),(0,0,255),3)
        cv2.circle(image_copy,tuple(top),2,(255,255,255), 10)#drawing the top circle
        cv2.circle(image_copy,tuple(bottom),2,(255,255,255), 10)#drawing the bottom circle
        

        
    #print(width)
    #print(height)
    #image_copy=contours(image,image_copy)
    cv2.circle(image_copy,(429,102),2,(255,0,255), 5)
    cv2.circle(image_copy,(700,836),2,(255,0,255), 5)
    #cv2.circle(image_copy,tuple(centre),2,(255,255,255), 10)
    cv2.imshow('gray scale',image_copy)
    cv2.waitKey(0)


def DistanceAndAngles(middleX,image_copy):
    z=0
    count=0
    c=[[],[]]
    global Improved
    for b in range(len(IMGcontours)):
        for n in range(len(IMGcontours[b])):
            if(count == 300):
                #print(IMGcontours[b][n-1][0])
                #print(middleX)
                c[0].append(math.sqrt((middleX[0][0]-IMGcontours[b][n-1][0][0])**2+(middleX[1][0]-IMGcontours[b][n-1][0][1])**2))

                c[1].append(math.degrees(math.atan((-middleX[1][0]+IMGcontours[b][n-1][0][1])/(-middleX[0][0]+IMGcontours[b][n-1][0][0]))))
                
                cv2.circle(image_copy,tuple(IMGcontours[b][n-1][0]),2,(255,0,255), 5)
                count=0
            else:
                count=count+1
    print(c[1])


    #cv2.imshow('gray scale',image_copy)
    #cv2.waitKey(0)







def Contours(image):
    image=gray(image)
    global contours_poly
    global IMGcontours
    #global Improved
    IMGcontours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, IMGcontours, -1, (0, 255, 0), 3)
    cv2.imshow('gray scale',image)
    cv2.waitKey(0)
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
    #file=open("contours.txt","w")
    #print(len(IMGcontours[2]))
    print(IMGcontours[4][3][0][0])#range from 0-4    327,107
    #z=np.where(IMGcontours[4][3][0]==101)
    #print(z[0].size)
    # Draw polygonal contour + bonding rects + circles
    color=(256,250,256)
    for i in range(len(IMGcontours)):
        if(int(boundRect[i][3])>=250):
            cv2.drawContours(drawing, contours_poly, i, color)
            cv2.circle(drawing, (int(centers[i][0]), int(centers[i][1])), 10, color, 2)
            middleX=(int(centers[i][0]), int(centers[i][1]))
            
    return middleX,drawing


Main()

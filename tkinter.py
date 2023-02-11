import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import cv2

class GUI_Window():
    def __init__(self):
        self.window=tk.Tk()
        self.window.title('OpenCV GUI')
    
        

        self.canv,self.canv2=self.DeclareCanvas(self.window)
        image=cv2.imread('test_image.jpg')
        image2=cv2.imread('test_image2.jpg')
        img=self.FormatImageCanvas(image)
        img2=self.FormatImageCanvas(image2)
        self.Canv(img,img2,self.canv,self.canv2)
        
        #Updates Window
        self.UpdateGUI()
        
    def DeclareCanvas(self,window):
        self.canv = Canvas(window, width=448, height=336, bg='white')
        self.canv2 = Canvas(window, width=448, height=336, bg='white')
        self.canv.grid(row=1, column=0, columnspan=2)
        self.canv2.grid(row=1, column=3, columnspan=4)
        return self.canv,self.canv2
    
    def FormatImageCanvas(self,img):
        #Note: this line is need down below or else blue and red switch. could be useful
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img,(448,336))
        img=Image.fromarray(img)
        img=ImageTk.PhotoImage(img)
        return 0
    
    def Canv(self,img,img2,canv,canv2):
        self.canv.create_image((224,168),image=img)
        self.canv2.create_image((224,168),image=img2)
        
    def UpdateGUI(self):
        self.window.after(1000, self.UpdateGUI)
        return 0
    

def main():
    GUI=GUI_Window()
    #GUI.mainloop()
    
if __name__=="__main__":
    main()

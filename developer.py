from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")


        logo_img = Image.open(r"images\Logo.png")
        logo_img = logo_img.resize((130, 130))  # Adjust the size as needed
        self.logo_photo = ImageTk.PhotoImage(logo_img)

        # Display the college logo
        logo_label = Label(self.root, image=self.logo_photo)
        logo_label.place(x=10, y=10)

        # Add the college name
        college_name_label = Label(self.root, text="Noida Institute of Engineering and Technology", font=("Arial", 45, "bold"))
        college_name_label.place(x=160, y=10)
        college_tagline = Label(self.root, text="Greater Noida | An Autonomous Institute", font=("Arial", 20, "bold"))
        college_tagline.place(x=500, y=90)

        #background image
        img3 = Image.open(r"images\Background.png")
        img3 = img3.resize((1530,710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #title
        title_lbl = Label(bg_img,text="Developer", font=("Georgia",27,"bold"),bg="#CB2D6F",fg="White")
        title_lbl.place(x = 0, y = 0,width=1530,height=45)

        #main frame Roshan
        main_frame = Frame(bg_img,bd=2,bg="White")
        main_frame.place(x=10,y=60,width=750,height=580)
        dev1_img=Image.open(r"images\dev1.png")
        dev1_img=dev1_img.resize((200,200))
        self.photoimg_dev1=ImageTk.PhotoImage(dev1_img)

        f_lbl=Label(main_frame,image=self.photoimg_dev1)
        f_lbl.place(x=275,y=0,width=200,height=200)

        #Developer1 info

        dev1_label = Label(main_frame,text="Hello, My name is Roshan Kumar Singh.",font=("Georgia",20,"bold"),bg="White",fg="#33a9ab")
        dev1_label.place(x=0,y=205)

        dev1_label = Label(main_frame,text="About:",font=("Georgia",15,"bold"),bg="White",fg="#33a9ab")
        dev1_label.place(x=0,y=250)
        dev1_label = Label(main_frame,text=">>>>> Software developer based in Greater Noida, India.",font=("Calibri",13,"bold"),bg="White")
        dev1_label.place(x=0,y=275)
        dev1_label = Label(main_frame,text=">>>>> Artificial Intelligence & Machine Learning undergraduate from NIET.",font=("Calibri",13,"bold"),bg="White")
        dev1_label.place(x=0,y=300)
        dev1_label = Label(main_frame,text=">>>>> Passionate about coding and software development.",font=("Calibri",13,"bold"),bg="White")
        dev1_label.place(x=0,y=325)
        dev1_label = Label(main_frame,text=">>>>> Working for myself to improve my skills.",font=("Calibri",13,"bold"),bg="White")
        dev1_label.place(x=0,y=350)

        dev1_label = Label(main_frame,text="Skills:",font=("Georgia",15,"bold"),bg="White",fg="#33a9ab")
        dev1_label.place(x=0,y=400)
        #row1
        dev1_label = Label(main_frame,text="Python",font=("Calibri",13,"bold"),bg="White")
        dev1_label.place(x=10,y=425,)
        dev1_label = Label(main_frame,text="C Programming",font=("Calibri",13,"bold"),bg="White")
        dev1_label.place(x=195,y=425,)
        dev1_label = Label(main_frame,text="Machine Learning",font=("Calibri",13,"bold"),bg="White")
        dev1_label.place(x=380,y=425,)
        dev1_label = Label(main_frame,text="Data Structures",font=("Calibri",13,"bold"),bg="White")
        dev1_label.place(x=565,y=425,)

        #row2
        dev1_label = Label(main_frame,text="Algorithm",font=("Calibri",13,"bold"),bg="White")
        dev1_label.place(x=10,y=450,)
        dev1_label = Label(main_frame,text="Object Oriented P.",font=("Calibri",13,"bold"),bg="White")
        dev1_label.place(x=195,y=450,)
        dev1_label = Label(main_frame,text="HTML",font=("Calibri",13,"bold"),bg="White")
        dev1_label.place(x=380,y=450,)
        dev1_label = Label(main_frame,text="CSS",font=("Calibri",13,"bold"),bg="White")
        dev1_label.place(x=565,y=450,)

        #row3
        dev1_label = Label(main_frame,text="Javascript",font=("Calibri",13,"bold"),bg="White")
        dev1_label.place(x=10,y=475,)
        dev1_label = Label(main_frame,text="Problem Solving",font=("Calibri",13,"bold"),bg="White")
        dev1_label.place(x=195,y=475,)
        dev1_label = Label(main_frame,text="Analytical Skills",font=("Calibri",13,"bold"),bg="White")
        dev1_label.place(x=380,y=475,)
        dev1_label = Label(main_frame,text="Communication Skills",font=("Calibri",13,"bold"),bg="White")
        dev1_label.place(x=565,y=475,)





        #main frame Uttam
        main_frame2 = Frame(bg_img,bd=2,bg="White")
        main_frame2.place(x=770,y=60,width=750,height=580)
        dev2_img=Image.open(r"images\dev2.png")
        dev2_img=dev2_img.resize((200,200))
        self.photoimg_dev2=ImageTk.PhotoImage(dev2_img)

        f_lbl=Label(main_frame2,image=self.photoimg_dev2)
        f_lbl.place(x=275,y=0,width=200,height=200)

        #Developer2 info

        dev2_label = Label(main_frame2,text="Hello, My name is Uttam Vashishth.",font=("Georgia",20,"bold"),bg="White",fg="#33a9ab")
        dev2_label.place(x=0,y=205)

        dev2_label = Label(main_frame2,text="About:",font=("Georgia",15,"bold"),bg="White",fg="#33a9ab")
        dev2_label.place(x=0,y=250)
        dev2_label = Label(main_frame2,text=">>>>> Software developer based in Greater Noida, India.",font=("Calibri",13,"bold"),bg="White")
        dev2_label.place(x=0,y=275)
        dev2_label = Label(main_frame2,text=">>>>> Artificial Intelligence & Machine Learning undergraduate from NIET.",font=("Calibri",13,"bold"),bg="White")
        dev2_label.place(x=0,y=300)
        dev2_label = Label(main_frame2,text=">>>>> Passionate about coding and software development.",font=("Calibri",13,"bold"),bg="White")
        dev2_label.place(x=0,y=325)
        dev2_label = Label(main_frame2,text=">>>>> Working for myself to improve my skills.",font=("Calibri",13,"bold"),bg="White")
        dev2_label.place(x=0,y=350)

        dev2_label = Label(main_frame2,text="Skills:",font=("Georgia",15,"bold"),bg="White",fg="#33a9ab")
        dev2_label.place(x=0,y=400)
        #row1
        dev2_label = Label(main_frame2,text="Python",font=("Calibri",13,"bold"),bg="White")
        dev2_label.place(x=10,y=425,)
        dev2_label = Label(main_frame2,text="C Programming",font=("Calibri",13,"bold"),bg="White")
        dev2_label.place(x=195,y=425,)
        dev2_label = Label(main_frame2,text="Machine Learning",font=("Calibri",13,"bold"),bg="White")
        dev2_label.place(x=380,y=425,)
        dev2_label = Label(main_frame2,text="Data Structures",font=("Calibri",13,"bold"),bg="White")
        dev2_label.place(x=565,y=425,)

        #row2
        dev2_label = Label(main_frame2,text="Algorithm",font=("Calibri",13,"bold"),bg="White")
        dev2_label.place(x=10,y=450,)
        dev2_label = Label(main_frame2,text="Object Oriented P.",font=("Calibri",13,"bold"),bg="White")
        dev2_label.place(x=195,y=450,)
        dev2_label = Label(main_frame2,text="HTML",font=("Calibri",13,"bold"),bg="White")
        dev2_label.place(x=380,y=450,)
        dev2_label = Label(main_frame2,text="CSS",font=("Calibri",13,"bold"),bg="White")
        dev2_label.place(x=565,y=450,)

        #row3
        dev2_label = Label(main_frame2,text="Javascript",font=("Calibri",13,"bold"),bg="White")
        dev2_label.place(x=10,y=475,)
        dev2_label = Label(main_frame2,text="Problem Solving",font=("Calibri",13,"bold"),bg="White")
        dev2_label.place(x=195,y=475,)
        dev2_label = Label(main_frame2,text="Analytical Skills",font=("Calibri",13,"bold"),bg="White")
        dev2_label.place(x=380,y=475,)
        dev2_label = Label(main_frame2,text="Communication Skills",font=("Calibri",13,"bold"),bg="White")
        dev2_label.place(x=565,y=475,)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
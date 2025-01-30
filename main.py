from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
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
        college_tagline.place(x=560, y=90)


        #background image
        img3 = Image.open(r"images\Background.png")
        img3 = img3.resize((1530,710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #title
        title_lbl = Label(bg_img,text="Face Recognition Attendance System Software", font=("Georgia",30,"bold"),bg="#CB2D6F",fg="White")
        title_lbl.place(x = 0, y = 0,width=1530,height=45)

        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl = Label(title_lbl,font=("Georgia",15,"bold"),bg="#CB2D6F",fg="White")
        lbl.place(x = 0, y = 0,width=150,height=45)
        time()



        #student button
        img4 = Image.open(r"images\StudentDetails.png")
        img4 = img4.resize((220,220))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x = 200,y=100,width=220,height=220)
        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Georgia",15,"bold"),bg="Grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        b1_1.place(x = 200,y=300,width=220,height=40)


        #Detect face button
        img5 = Image.open(r"images\FaceDetector.png")
        img5 = img5.resize((220,220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x = 500,y=100,width=220,height=220)
        b1_1 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("Georgia",15,"bold"),bg="Grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        b1_1.place(x = 500,y=300,width=220,height=40)


        #Attendance button
        img6 = Image.open(r"images\Attendance.png")
        img6 = img6.resize((220,220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x = 800,y=100,width=220,height=220)
        b1_1 = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("Georgia",15,"bold"),bg="Grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        b1_1.place(x = 800,y=300,width=220,height=40)


        #Help button
        img7 = Image.open(r"images\Helpdesk.png")
        img7 = img7.resize((220,220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help)
        b1.place(x = 1100,y=100,width=220,height=220)
        b1_1 = Button(bg_img,text="Help Desk",cursor="hand2",command=self.help,font=("Georgia",15,"bold"),bg="Grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        b1_1.place(x = 1100,y=300,width=220,height=40)


        #train data button
        img8 = Image.open(r"images\TrainData.png")
        img8 = img8.resize((220,220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x = 200,y=380,width=220,height=220)
        b1_1 = Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("Georgia",15,"bold"),bg="Grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        b1_1.place(x = 200,y=580,width=220,height=40)


        #photos button
        img9 = Image.open(r"images\Photos.png")
        img9 = img9.resize((220,220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x = 500,y=380,width=220,height=220)
        b1_1 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("Georgia",15,"bold"),bg="Grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        b1_1.place(x = 500,y=580,width=220,height=40)


        #developer button
        img10 = Image.open(r"images\Developer.png")
        img10 = img10.resize((220,220))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x = 800,y=380,width=220,height=220)
        b1_1 = Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("Georgia",15,"bold"),bg="Grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        b1_1.place(x = 800,y=580,width=220,height=40)


        #exit button
        img11 = Image.open(r"images\exit.png")
        img11 = img11.resize((220,220))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x = 1100,y=380,width=220,height=220)
        b1_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("Georgia",15,"bold"),bg="Grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        b1_1.place(x = 1100,y=580,width=220,height=40)


    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

    #Function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

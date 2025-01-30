from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
class Train:
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
        title_lbl = Label(bg_img,text="Train Dataset", font=("Georgia",27,"bold"),bg="#CB2D6F",fg="White")
        title_lbl.place(x = 0, y = 0,width=1530,height=45)

        #first image
        img_top = Image.open(r"images\TrainDataTop.png")
        img_top = img_top.resize((1530,332))
        self.photoimg = ImageTk.PhotoImage(img_top)

        top_lbl = Label(bg_img,image = self.photoimg)
        top_lbl.place(x=0,y=45,width=1530,height=300)
        
        #train data button

        train_button = Button(bg_img,text="Train Data",command=self.train_classifier,cursor="hand2",font=("Georgia",30,"bold"),bg="Grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        train_button.place(x = 10,y=345,width=1500,height=45)
        #second image
        img_bottom = Image.open(r"images\TrainDataBottom.png")
        img_bottom = img_bottom.resize((1530,330))
        self.photoimgbottom = ImageTk.PhotoImage(img_bottom)

        bottom_lbl = Label(bg_img,image = self.photoimgbottom)
        bottom_lbl.place(x=0,y=390,width=1530,height=300)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)



        #train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed !!!")








if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
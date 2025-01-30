#line 102
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.root.wm_iconbitmap("face.ico")


        self.bg=ImageTk.PhotoImage(file=r"images\LoginBackground.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=1010,y=105,width=340,height=450)

        img1=Image.open(r"images\LoginImage.png")
        img1=img1.resize((100,100),Image.Resampling.HAMMING)
        self.photoimage1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=1130,y=110,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("Calibri",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)

        #label
        username_lbl=Label(frame,text="Username",font=("Calibri",15),fg="black",bg="white")
        username_lbl.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("Calibri",15))
        self.txtuser.place(x=40,y=180,width=270)

        password_lbl=Label(frame,text="Password",font=("Calibri",15),fg="black",bg="white")
        password_lbl.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("Calibri",15))
        self.txtpass.place(x=40,y=250,width=270)

        #icon images

        img2=Image.open(r"images\UsernameImage.png")
        img2=img2.resize((25,25))
        self.photoimage2=ImageTk.PhotoImage(img2)

        lblimg2=Label(image=self.photoimage2,bg="white",borderwidth=0)
        lblimg2.place(x=1050,y=258,width=25,height=25)

        img3=Image.open(r"images\PasswordImage.png")
        img3=img3.resize((25,25))
        self.photoimage3=ImageTk.PhotoImage(img3)

        lblimg3=Label(image=self.photoimage3,bg="white",borderwidth=0)
        lblimg3.place(x=1050,y=330,width=25,height=25)


        #buttons
        #login button
        loginbtn=Button(frame,text="Login",command=self.login,font=("Calibri",15),bd=3,relief=RIDGE,fg="white",bg="#CB2D6F",activebackground="#CB2D6F",activeforeground="white")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("Calibri",10),bd=3,borderwidth=0,fg="#3457D5",bg="white",activebackground="white",activeforeground="#3457D5")
        registerbtn.place(x=20,y=350,width=160)

        #forgot password button
        registerbtn=Button(frame,text="Forgot Password?",command=self.forgot_password_window,font=("Calibri",10),bd=3,borderwidth=0,fg="#3457D5",bg="white",activebackground="white",activeforeground="#3457D5")
        registerbtn.place(x=20,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass=="":
            messagebox.showerror("Error","ALL fields required")
        elif (self.txtuser.get()=="rosh" and self.txtpass.get()=="singh"):
            messagebox.showinfo("Success","Welcome")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="login_form")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where Email=%s and Password=%s",(self.txtuser.get(),self.txtpass.get()))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username or password")
            else:
                open_main=messagebox.askyesno("Yes/No","Admin access only")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #reset password
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="login_form")
            my_cursor=conn.cursor()
            qury=("select * from register where Email=%s and SecurityQ=%s and SecurityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer.",parent=self.root2)
            else:
                query=("update register set Password=%s where Email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your password has been reset successfully.",parent=self.root2)
                self.root2.destroy()


    


    #forgot password window
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset the password.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="login_form")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("My Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel(bg="white")
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("Calibri",15,"bold"),fg="white",bg="#cb2d6f")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("Calibri",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)
                self.combo_security_Q=ttk.Combobox(self.root2,font=("Calibri",15),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2,text="Security Answer",font=("Calibri",15,"bold"),bg="white")
                security_A.place(x=50,y=150)
                self.txt_security=ttk.Entry(self.root2,font=("Calibri",15))
                self.txt_security.place(x=50,y=180,width=250)



                new_password=Label(self.root2,text="New Password",font=("Calibri",15,"bold"),bg="white")
                new_password.place(x=50,y=220)
                self.txt_new_password=ttk.Entry(self.root2,font=("Calibri",15))
                self.txt_new_password.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("Calibri",15,"bold"),fg="white",bg="#cb2d6f")
                btn.place(x=150,y=290)






class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        self.root.wm_iconbitmap("face.ico")

        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()

        #bg image
        self.bg=ImageTk.PhotoImage(file=r"images\RegisterBackground.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #left image
        self.bg1=ImageTk.PhotoImage(file=r"images\Register.png")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=5,y=100,width=470,height=550)

        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)


        register_lbl=Label(frame,text="REGISTER HERE",font=("Georgia",20,"bold"),fg="#33a9ab",bg="white")
        register_lbl.place(x=20,y=20)

        #label and entry
        #row 1
        fname=Label(frame,text="First Name",font=("Calibri",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Calibri",15))
        fname_entry.place(x=50,y=130,width=250)


        l_name=Label(frame,text="Last Name",font=("Calibri",15,"bold"),bg="white")
        l_name.place(x=370,y=100)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("Calibri",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #row 2
        contact=Label(frame,text="Contact No",font=("Calibri",15,"bold"),bg="white")
        contact.place(x=50,y=170)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("Calibri",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("Calibri",15,"bold"),bg="white")
        email.place(x=370,y=170)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("Calibri",15))
        self.txt_email.place(x=370,y=200,width=250)

        #row 3
        security_Q=Label(frame,text="Select Security Question",font=("Calibri",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("Calibri",15),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("Calibri",15,"bold"),bg="white")
        security_A.place(x=370,y=240)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("Calibri",15))
        self.txt_security.place(x=370,y=270,width=250)


        #row 4
        pswd=Label(frame,text="Password",font=("Calibri",15,"bold"),bg="white")
        pswd.place(x=50,y=310)
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("Calibri",15))
        self.txt_pswd.place(x=50,y=340,width=250)


        confirm_pswd=Label(frame,text="Confirm Password",font=("Calibri",15,"bold"),bg="white")
        confirm_pswd.place(x=370,y=310)
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("Calibri",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)


        #check button
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the terms & conditions.",font=("Calibri",12),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)


        #buttons
        img=Image.open(r"images\Register Now.png")
        img=img.resize((200,45))
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=50,y=420,width=200)


        img1=Image.open(r"images\Login Now.png")
        img1=img1.resize((200,45))
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=370,y=420,width=200)

    #function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error","Password & confirm passowrd must be same.",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions.",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="login_form")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","User already exist. Please try another email.",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_securityQ.get(),self.var_securityA.get(),self.var_pass.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration Successfull.")



    def return_login(self):
        self.root.destroy()






if __name__ == "__main__":
    main()
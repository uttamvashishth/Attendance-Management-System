from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")


        #variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()


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
        title_lbl = Label(bg_img,text="Student Management System", font=("Georgia",27,"bold"),bg="#CB2D6F",fg="White")
        title_lbl.place(x = 0, y = 0,width=1530,height=45)


        #main frame
        main_frame = Frame(bg_img,bd=2,bg="White")
        main_frame.place(x=20,y=50,width=1480,height=600)


        #left label frame
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Georgia",12,"bold"),bg="White")
        left_frame.place(x=10,y=10,width=730,height=580)

        #left label image
        img_left = Image.open(r"images\LeftLabelImage.png")
        img_left = img_left.resize((720,130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame,image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #current course information
        current_course_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("Georgia",12,"bold"),bg="white")
        current_course_frame.place(x=5,y=135,width=720,height=115)

        #department
        dep_label = Label(current_course_frame,text="Department",font=("Georgia",13,"bold"),bg="White")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("Georgia",13,"bold"),width=14,state="readonly")
        dep_combo["values"] = ("Select Department","AIML","CSE","AI","IOT","Civil","Mechanical","CS")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #course
        course_label = Label(current_course_frame,text="Course",font=("Georgia",13,"bold"),bg="White")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Georgia",13,"bold"),width=14,state="readonly")
        course_combo["values"] = ("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #year
        year_label = Label(current_course_frame,text="Year",font=("Georgia",13,"bold"),bg="White")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Georgia",13,"bold"),width=14,state="readonly")
        year_combo["values"] = ("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #semester
        semester_label = Label(current_course_frame,text="Semester",font=("Georgia",13,"bold"),bg="White")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("Georgia",13,"bold"),width=14,state="readonly")
        semester_combo["values"] = ("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #class student information
        class_student_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("Georgia",12,"bold"),bg="white")
        class_student_frame.place(x=5,y=250,width=720,height=300)

        #student id
        studentId_label = Label(class_student_frame,text="StudentID:",font=("Georgia",13,"bold"),bg="White")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=14,font=("Georgia",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #student name
        studentName_label = Label(class_student_frame,text="Student Name:",font=("Georgia",13,"bold"),bg="White")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=14,font=("Georgia",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #class division
        class_div_label = Label(class_student_frame,text="Class Division:",font=("Georgia",13,"bold"),bg="White")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        
        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("Georgia",13,"bold"),width=13,state="readonly")
        div_combo["values"] = ("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll no
        roll_no_label = Label(class_student_frame,text="Roll No:",font=("Georgia",13,"bold"),bg="White")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=14,font=("Georgia",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label = Label(class_student_frame,text="Gender:",font=("Georgia",13,"bold"),bg="White")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Georgia",13,"bold"),width=13,state="readonly")
        gender_combo["values"] = ("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)



        #DOB
        dob_label = Label(class_student_frame,text="DOB:",font=("Georgia",13,"bold"),bg="White")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=14,font=("Georgia",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #email
        email_label = Label(class_student_frame,text="Email:",font=("Georgia",13,"bold"),bg="White")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=14,font=("Georgia",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #pnone no
        phone_label = Label(class_student_frame,text="Phone No:",font=("Georgia",13,"bold"),bg="White")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=14,font=("Georgia",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #Address
        address_label = Label(class_student_frame,text="Address:",font=("Georgia",13,"bold"),bg="White")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=14,font=("Georgia",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #teacher name
        teacher_label = Label(class_student_frame,text="Teacher Name:",font=("Georgia",13,"bold"),bg="White")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=14,font=("Georgia",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        #radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #buttons frame
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        #save button
        save_btn = Button(btn_frame,command=self.add_data,text="Save",width=14,font=("Georgia",13,"bold"),bg="grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        save_btn.grid(row=0,column=0)
        #update button
        update_btn = Button(btn_frame,command=self.update_data,text="Update",width=14,font=("Georgia",13,"bold"),bg="grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        update_btn.grid(row=0,column=1)
        #delete button
        delete_btn = Button(btn_frame,command=self.delete_data,text="Delete",width=14,font=("Georgia",13,"bold"),bg="grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        delete_btn.grid(row=0,column=2)
        #reset button
        reset_btn = Button(btn_frame,command=self.reset_data,text="Reset",width=14,font=("Georgia",13,"bold"),bg="grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        reset_btn.grid(row=0,column=3)


        #take/update photo sample buttons frame
        btn_frame1 = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)
        #take photo sample button
        take_photo_btn = Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=29,font=("Georgia",13,"bold"),bg="grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        take_photo_btn.grid(row=0,column=0)
        #update photo sample button
        update_photo_btn = Button(btn_frame1,text="Update Photo Sample",width=29,font=("Georgia",13,"bold"),bg="grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        update_photo_btn.grid(row=0,column=1)




        #right label frame
        right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Georgia",12,"bold"),bg="white")
        right_frame.place(x=750,y=10,width=720,height=580)

        #rightt label image
        img_right = Image.open(r"images\LeftLabelImage.png")
        img_right = img_right.resize((710,130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame,image = self.photoimg_right)
        f_lbl.place(x=5,y=0,width=710,height=130)


        #search system
        search_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("Georgia",12,"bold"),bg="white")
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label = Label(search_frame,text="Search By:",font=("Georgia",11,"bold"),bg="grey",fg="white")
        search_label.grid(row=0,column=0,padx=4,pady=5,sticky=W)


        search_combo = ttk.Combobox(search_frame,font=("Georgia",13,"bold"),width=11,state="readonly")
        search_combo["values"] = ("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        search_entry = ttk.Entry(search_frame,width=11,font=("Georgia",13,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=5,sticky=W)




        #delete button
        search_btn = Button(search_frame,text="Delete",width=11,font=("Georgia",13,"bold"),bg="grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        search_btn.grid(row=0,column=3,padx=4)
        #reset button
        showAll_btn = Button(search_frame,text="Reset",width=11,font=("Georgia",13,"bold"),bg="grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        showAll_btn.grid(row=0,column=4,padx=4)


        #table frame
        table_frame = Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=210,width=710,height=350)
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #function declaration to add data
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #function declaration to fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # get cursor
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    #update data funtion
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent = self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update:
                    conn = mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get()))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    #delete data function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete?","Do you want to delete this student?",parent=self.root)
                if delete:
                    conn = mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success","Student details successfully deleted",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #reset button funtion
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #generate dataset take photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get()==id+1))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #load predefined data on face frontals from open cv 2
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)#1.3=scaling factor, 5=minimum neighbor
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face= cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed !!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 

                    
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
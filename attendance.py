from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")


        #variables
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()



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
        title_lbl = Label(bg_img,text="Attendance Management System", font=("Georgia",27,"bold"),bg="#CB2D6F",fg="White")
        title_lbl.place(x = 0, y = 0,width=1530,height=45)

        #main frame
        main_frame = Frame(bg_img,bd=2,bg="White")
        main_frame.place(x=20,y=50,width=1480,height=600)

        #left label frame
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("Georgia",12,"bold"),bg="White")
        left_frame.place(x=10,y=10,width=730,height=580)

        #left label image
        img_left = Image.open(r"images\AttendanceLeftLabelImage.png")
        img_left = img_left.resize((720,130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame,image = self.photoimg_left)
        f_lbl.place(x=3,y=0,width=720,height=130)

        #left inside frame
        left_inside_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="White")
        left_inside_frame.place(x=0,y=135,width=725,height=370)

        #lables and entries
        #attendance id
        attendanceId_label = Label(left_inside_frame,text="AttendanceID:",font=("Georgia",13,"bold"),bg="White")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame,width=14,textvariable=self.var_attend_id,font=("Georgia",13,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll no
        rollLabel = Label(left_inside_frame,text="Roll:",font=("Georgia",13,"bold"),bg="White")
        rollLabel.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        atten_roll = ttk.Entry(left_inside_frame,width=14,textvariable=self.var_attend_roll,font=("Georgia",13,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Name
        nameLabel = Label(left_inside_frame,text="Name:",font=("Georgia",13,"bold"),bg="White")
        nameLabel.grid(row=1,column=0)

        atten_name = ttk.Entry(left_inside_frame,width=14,textvariable=self.var_attend_name,font=("Georgia",13,"bold"))
        atten_name.grid(row=1,column=1,pady=8)

        #Department
        depLabel = Label(left_inside_frame,text="Department:",font=("Georgia",13,"bold"),bg="White")
        depLabel.grid(row=1,column=2)

        atten_dep = ttk.Entry(left_inside_frame,width=14,textvariable=self.var_attend_dep,font=("Georgia",13,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)

        #time
        timeLabel = Label(left_inside_frame,text="Time:",font=("Georgia",13,"bold"),bg="White")
        timeLabel.grid(row=2,column=0)

        atten_dep = ttk.Entry(left_inside_frame,width=14,textvariable=self.var_attend_time,font=("Georgia",13,"bold"))
        atten_dep.grid(row=2,column=1,pady=8)

        #Date
        dateLabel = Label(left_inside_frame,text="Date:",font=("Georgia",13,"bold"),bg="White")
        dateLabel.grid(row=2,column=2)

        atten_date = ttk.Entry(left_inside_frame,width=14,textvariable=self.var_attend_date,font=("Georgia",13,"bold"))
        atten_date.grid(row=2,column=3,pady=8)

        #Attendance
        attendanceLabel = Label(left_inside_frame,text=" Attendance Status:",font=("Georgia",13,"bold"),bg="White")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=13,textvariable=self.var_attend_attendance,font=("Georgia",13,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #buttons frame
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        #import button
        import_btn = Button(btn_frame,text="Import csv",command=self.importCsv,width=14,font=("Georgia",13,"bold"),bg="grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        import_btn.grid(row=0,column=0)
        #export button
        export_btn = Button(btn_frame,text="Export csv",command=self.exportCsv,width=14,font=("Georgia",13,"bold"),bg="grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        export_btn.grid(row=0,column=1)
        #update button
        update_btn = Button(btn_frame,text="Update",width=14,font=("Georgia",13,"bold"),bg="grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        update_btn.grid(row=0,column=2)
        #reset button
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("Georgia",13,"bold"),bg="grey",fg="white",activebackground="#CB2D6F",activeforeground="White")
        reset_btn.grid(row=0,column=3)

        #right label frame
        right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("Georgia",12,"bold"),bg="white")
        right_frame.place(x=750,y=10,width=720,height=580)

        #right inside frame
        table_frame = Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=705,height=455)

        #scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")


            




if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        # College logo
        logo_img = Image.open(r"images\Logo.png")
        logo_img = logo_img.resize((130, 130))  # Adjust the size as needed
        self.logo_photo = ImageTk.PhotoImage(logo_img)
        logo_label = Label(self.root, image=self.logo_photo)
        logo_label.place(x=10, y=10)

        # College name and tagline
        college_name_label = Label(self.root, text="Noida Institute of Engineering and Technology", font=("Arial", 45, "bold"), fg="#003366")
        college_name_label.place(x=160, y=10)
        college_tagline = Label(self.root, text="Greater Noida | An Autonomous Institute", font=("Arial", 20, "bold"), fg="#003366")
        college_tagline.place(x=500, y=90)

        # Background image
        img3 = Image.open(r"images\Background.png")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title
        title_lbl = Label(bg_img, text="Help Desk", font=("Georgia", 27, "bold"), bg="#CB2D6F", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Create and place labels and entry fields for the helpdesk form
        self.create_helpdesk_form(bg_img)

    def create_helpdesk_form(self, parent):
        # Form frame
        form_frame = Frame(parent, bg="white", bd=2, relief=RIDGE)
        form_frame.place(x=450, y=100, width=600, height=400)

        # Form title
        form_title = Label(form_frame, text="Submit Your Query", font=("Helvetica", 16, "bold"), bg="white", fg="#003366")
        form_title.grid(row=0, columnspan=2, pady=10)

        # User's name
        name_label = Label(form_frame, text="Name:", font=("Helvetica", 14), bg="white")
        name_label.grid(row=1, column=0, padx=20, pady=10, sticky=E)
        self.name_entry = Entry(form_frame, font=("Helvetica", 14), width=30, bd=2, relief=SUNKEN)
        self.name_entry.grid(row=1, column=1, padx=20, pady=10, sticky=W)

        # User's email
        email_label = Label(form_frame, text="Email:", font=("Helvetica", 14), bg="white")
        email_label.grid(row=2, column=0, padx=20, pady=10, sticky=E)
        self.email_entry = Entry(form_frame, font=("Helvetica", 14), width=30, bd=2, relief=SUNKEN)
        self.email_entry.grid(row=2, column=1, padx=20, pady=10, sticky=W)

        # User's query
        query_label = Label(form_frame, text="Query:", font=("Helvetica", 14), bg="white")
        query_label.grid(row=3, column=0, padx=20, pady=10, sticky=NE)
        self.query_text = Text(form_frame, font=("Helvetica", 14), width=30, height=5, bd=2, relief=SUNKEN)
        self.query_text.grid(row=3, column=1, padx=20, pady=10, sticky=W)

        # Submit button
        submit_button = Button(form_frame, text="Submit", font=("Helvetica", 14, "bold"), bg="#CB2D6F", fg="white", command=self.submit_query)
        submit_button.grid(row=4, column=1, padx=20, pady=20, sticky=E)

        # Add hover effect to the button
        submit_button.bind("<Enter>", lambda e: submit_button.config(bg="#A51D49"))
        submit_button.bind("<Leave>", lambda e: submit_button.config(bg="#CB2D6F"))

    def submit_query(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        query = self.query_text.get("1.0", END).strip()

        # Simple validation
        if not name or not email or not query:
            messagebox.showerror("Error", "All fields are required")
            return

        # Send email
        self.send_email(name, email, query)

        # Clear the form
        self.name_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.query_text.delete("1.0", END)

        messagebox.showinfo("Success", "Your query has been submitted successfully")

    def send_email(self, name, email, query):
        from_email = "roshansonweb@gmail.com"  # Replace with your email
        from_password = "jwsz dkoe kcrw evxu"  # Replace with your app-specific password
        to_email = "0201csml191@niet.co.in"

        subject = "New Help Desk Query"
        body = f"Name: {name}\nEmail: {email}\nQuery:\n{query}"

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_email, from_password)
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            print("Email sent successfully")
        except Exception as e:
            print(f"Failed to send email: {e}")
            messagebox.showerror("Error", "Failed to send email")

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()

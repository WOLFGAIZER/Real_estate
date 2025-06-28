from tkinter import *
from tkinter import messagebox
from database import *
from email_sender import *

class Registration:
    def __init__(self, person, window, canvas, old_frame,frame_canvas, background):
        self.person = person
        self.canvas = canvas
        self.old_frame = old_frame
        self.frame_canvas = frame_canvas
        self.background = background
        self.frame = Frame(window, bg="#273C28", highlightthickness=5, pady=10, padx=2, highlightbackground="grey")
        self.frame_structure()
        self.front_page_bg = PhotoImage(file="Matrix Real estate.png")

    def frame_structure(self):
        if self.person == "agent":
            column_span = 1
        else:
            column_span = 2
        self.reg_label = Label(self.frame, text="Registration", bg="#273C28", borderwidth=5,
                               font=("Georgia", 30, "bold"),
                               fg="#fff")
        self.reg_label.grid(row=0, column=0, columnspan=2, pady=10, padx=20)

        self.name_label = Label(self.frame, text="Full Name", fg="#fff", bg="#273C28",
                                font=("Courier", 16, "underline"))
        self.name_label.grid(row=1, column=0, columnspan=column_span)

        self.name_entry = Entry(self.frame, insertwidth=1, width=20, highlightthickness=2, highlightbackground="grey",
                                justify=CENTER, font=("Courier", 20, "normal"))
        self.name_entry.grid(row=2, column=0, pady=(2, 10), padx=10, columnspan=column_span)

        self.pn_label = Label(self.frame, text="Phone number", fg="#fff", bg="#273C28",
                              font=("Courier", 16, "underline"))
        self.pn_label.grid(row=3, column=0, columnspan=column_span)

        self.pn_entry = Entry(self.frame, insertwidth=1, width=20, highlightthickness=2,
                              highlightbackground="grey", justify=CENTER, font=("Courier", 20, "normal"))
        self.pn_entry.grid(row=4, column=0, pady=(2, 10), padx=10, columnspan=column_span)

        self.email_label = Label(self.frame, text="Email ID", fg="#fff", bg="#273C28",
                                 font=("Courier", 16, "underline"))
        self.email_label.grid(row=5, column=0, columnspan=column_span)

        self.email_entry = Entry(self.frame, insertwidth=1, width=20, highlightthickness=2,
                                 highlightbackground="grey", justify=CENTER, font=("Courier", 20, "normal"))
        self.email_entry.grid(row=6, column=0, pady=(2, 10), padx=10, columnspan=column_span)

        self.aadhar_label = Label(self.frame, text="Aadhar number", fg="#fff", bg="#273C28",
                                  font=("Courier", 16, "underline"))
        self.aadhar_label.grid(row=9, column=0, columnspan=2)
        self.aadhar_entry = Entry(self.frame, insertwidth=1, width=20, highlightthickness=2,
                                  highlightbackground="grey", justify=CENTER, font=("Courier", 20, "normal"),
                                  foreground="#d3d3d3")
        self.aadhar_entry.insert(0, "xxxx-xxxx-xxxx")
        self.aadhar_entry.bind("<Button-1>", self.on_aadhar_click)
        self.aadhar_entry.grid(row=10, column=0, pady=(2, 20), padx=10, columnspan=2)

        if self.person == "agent":
            self.un_label = Label(self.frame, text="Username", fg="#fff", bg="#273C28",
                                  font=("Courier", 16, "underline"))
            self.un_label.grid(row=1, column=1, columnspan=column_span)

            self.un_entry = Entry(self.frame, insertwidth=1, width=20, highlightthickness=2,
                                  highlightbackground="grey", justify=CENTER, font=("Courier", 20, "normal"))
            self.un_entry.grid(row=2, column=1, pady=(2, 10), padx=10, columnspan=column_span)

            self.pw_label = Label(self.frame, text="Password", fg="#fff", bg="#273C28",
                                  font=("Courier", 16, "underline"))
            self.pw_label.grid(row=3, column=1, columnspan=1)

            self.pw_entry = Entry(self.frame, show="*", insertwidth=1, width=20, highlightthickness=2,
                                  highlightbackground="grey", justify=CENTER, font=("Courier", 20, "normal"))
            self.pw_entry.grid(row=4, column=1, pady=(2, 10), padx=10)

            self.cpw_label = Label(self.frame, text="Confirm Password", fg="#fff", bg="#273C28",
                                   font=("Courier", 16, "underline"))
            self.cpw_label.grid(row=5, column=1, columnspan=1)

            self.cpw_entry = Entry(self.frame, show="*", insertwidth=1, width=20, highlightthickness=2,
                                   highlightbackground="grey", justify=CENTER, font=("Courier", 20, "normal"))
            self.cpw_entry.grid(row=6, column=1, pady=(2, 10), padx=10)

            self.locality_label = Label(self.frame, text="Locality", fg="#fff", bg="#273C28",
                                  font=("Courier", 16, "underline"))
            self.locality_label.grid(row=7, column=0, columnspan=column_span)

            self.locality_entry = Entry(self.frame, insertwidth=1, width=20, highlightthickness=2,
                                  highlightbackground="grey", justify=CENTER, font=("Courier", 20, "normal"))
            self.locality_entry.grid(row=8, column=0, pady=(2, 10), padx=10, columnspan=column_span)

            self.city_label = Label(self.frame, text="City", fg="#fff", bg="#273C28",
                                  font=("Courier", 16, "underline"))
            self.city_label.grid(row=7, column=1, columnspan=column_span)

            self.city_entry = Entry(self.frame, insertwidth=1, width=20, highlightthickness=2,
                                  highlightbackground="grey", justify=CENTER, font=("Courier", 20, "normal"))
            self.city_entry.grid(row=8, column=1, pady=(2, 10), padx=10, columnspan=column_span)

        if self.person != "agent":
            self.radio_value = StringVar(value="sellers")
            Radiobutton(self.frame, text="Owner", variable=self.radio_value, value="sellers", bg="#273C28", fg="#fff").grid(row=11, column=0, pady=(2, 10), padx=(160, 10))
            Radiobutton(self.frame, text="Purchaser", variable=self.radio_value, value="buyers", bg="#273C28", fg="#fff").grid(row=11, column=1, pady=(2, 10), padx=(10, 90))

        self.registration_button = Button(self.frame, text="Register", highlightthickness=0, width=15, height=2,
                                          highlightbackground="#273C28", font=("Courier", 20, "bold"),
                                          command=self.on_register_click)
        self.registration_button.grid(row=12, column=0, pady=(0, 0), columnspan=2)

        self.back_button = Button(self.frame, text=" 🔙 ", highlightthickness=0, width=2, height=2,
                                  highlightbackground="#273C28", font=("Courier", 15, "bold"), command=self.on_back_click)
        self.back_button.grid(row=13, column=1, pady=(0, 0), columnspan=1,padx=(260,20))

    def on_aadhar_click(self, event):
        if self.aadhar_entry.get() == "xxxx-xxxx-xxxx":
            self.aadhar_entry.delete(0, "end")
            self.aadhar_entry.config(foreground="#000000")

    def on_register_click(self):
        flag = 0
        if self.name_entry.get() == "" or self.pn_entry.get() == "" or self.email_entry.get() == "" or self.aadhar_entry.get() == "":
            messagebox.showwarning("Empty Entry", "Please enter all the fields.")
            flag = 1

        if len(self.pn_entry.get()) != 10 and flag == 0:
            messagebox.showwarning("Phone number", "Please enter 10 digit Phone number.")
            flag = 1

        if len(self.aadhar_entry.get()) != 12 and flag == 0:
            messagebox.showwarning("Aadhar number", "Please enter 12 digit Aadhar number.")
            flag = 1

        if self.person == "agent":
            if (self.un_entry.get() == "" or self.pw_entry.get() == "" or self.cpw_entry.get() == "" or self.locality_entry.get() == "" or self.city_entry.get() == "") and flag == 0:
                messagebox.showwarning("Empty Entry", "Please enter all the fields.")
                flag = 1

            if self.pw_entry.get() != self.cpw_entry.get() and flag == 0:
                messagebox.showwarning("Password confirmation", "The password doesn't match with the confirm password.")
                flag = 1

        # check for unique id with database
        if flag==0:
            flag, message = register_user("agents" if self.person=="agent" else self.radio_value.get(),
                                self.name_entry.get(), self.pn_entry.get(), self.email_entry.get(),
                                    self.aadhar_entry.get(), self.un_entry.get() if self.person=="agent" else "",
                                        self.pw_entry.get() if self.person=="agent" else "",
                                        f"{self.locality_entry.get()[0].upper()}{self.locality_entry.get()[1:]}, {self.city_entry.get()[0].upper()}{self.city_entry.get()[1:]}" if self.person=="agent"
                                        else "")
            
        if flag == 0:
            # if self.radio_value.get() == 1 buyer otherwise seller
            messagebox.showinfo("Registration", "Registered Successfully.\nA Mail has been sent to you for confirmation.")
            self.canvas.itemconfig(self.frame_canvas, window=self.old_frame, anchor="nw", )
            if self.person == "agent":
                self.canvas.coords(self.frame_canvas, 120, 100)
                self.canvas.itemconfig(self.background, image=self.front_page_bg)
            else:
                self.canvas.coords(self.frame_canvas, 200, 80)
        elif flag==1:
            messagebox.showwarning("Invalid Details", f"{message} already exists in the database!")
        elif flag==2:
            messagebox.showwarning("Already Registered", f"{message}")
            self.canvas.itemconfig(self.frame_canvas, window=self.old_frame, anchor="nw", )
            if self.person == "agent":
                self.canvas.coords(self.frame_canvas, 120, 100)
                self.canvas.itemconfig(self.background, image=self.front_page_bg)
            else:
                self.canvas.coords(self.frame_canvas, 200, 80)
        elif flag==3:
            messagebox.showwarning("Already Registered", f"{message}")

    def on_back_click(self):
        self.canvas.itemconfig(self.frame_canvas, window=self.old_frame, anchor="nw", )
        if self.person == "agent":
            self.canvas.coords(self.frame_canvas, 120, 100)
            self.canvas.itemconfig(self.background, image=self.front_page_bg)
        else:
            self.canvas.coords(self.frame_canvas, 200, 80)

















        # self.cpw_entry = None
        # self.cpw_label = None
        # self.pw_entry = None
        # self.pw_label = None
        # self.un_entry = None
        # self.un_label = None
        # self.aadhar_entry = None
        # self.aadhar_label = None
        # self.email_entry = None
        # self.email_label = None
        # self.pn_entry = None
        # self.pn_label = None
        # self.name_entry = None
        # self.name_label = None
        # self.registration_button = None
        # self.reg_label = None

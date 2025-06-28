from tkinter import *
from tkinter import messagebox,ttk
from database import *

class Property:
    def __init__(self, window, canvas, frame_canvas, old_frame):
        self.window = window
        self.canvas = canvas
        self.frame_canvas = frame_canvas
        self.old_frame = old_frame
        self.frame = Frame(window, bg="#273C28", highlightthickness=5, pady=5, padx=2, highlightbackground="grey")
        self.add_button = False
        self.remove_button = False
        self.frame_structure()

    def frame_structure(self):
        self.property_label = Label(self.frame, text="Property", bg="#273C28", borderwidth=5, font=("Georgia", 30, "bold italic"), fg="#fff")
        self.property_label.grid(row=0, column=0, columnspan=2, pady=(20,20), padx=20)
        self.canvas.coords(self.frame_canvas, 130, 80)
        self.radio_value = StringVar()
        self.add_radiobutton = Radiobutton(self.frame, text="Add", variable=self.radio_value, value="1", bg="#273C28", fg="#fff", command=self.add_property, font= ("Courier", 18, "normal"))
        self.add_radiobutton.grid(row=1,column=0, pady=(2, 10), padx=(100, 50),columnspan=1,)
        self.remove_radiobutton = Radiobutton(self.frame, text="Remove", variable=self.radio_value, value="2", bg="#273C28", fg="#fff", command=self.remove_property, font= ("Courier", 18, "normal"))
        self.remove_radiobutton.grid(row=1, column=1, pady=(2, 10), padx=(50, 100),columnspan=1,)
        self.remove_property()

    def add_property(self):
        self.add_button = True
        if self.remove_button:
            for widgets in self.frame.grid_slaves():
                widgets.grid_forget()
            self.property_label.grid(row=0, column=0, columnspan=3, pady=(0,10), padx=20)
            self.add_radiobutton.grid(row=1, column=0, pady=(2, 10), padx=(100, 50), columnspan=2, )
            self.remove_radiobutton.grid(row=1, column=1, pady=(2, 10), padx=(50, 100), columnspan=2, )

            self.remove_button = False
        self.canvas.coords(self.frame_canvas, 45, 20)

        Label(self.frame, text="House number", fg="#fff", bg="#273C28", font=("Courier", 16, "underline")).grid(row=5, column=0, columnspan=1)
        self.house_number = Entry(self.frame, insertwidth=1, width=13, highlightthickness=2, highlightbackground="grey",
                                justify=CENTER, font=("Courier", 20, "normal"))
        self.house_number.focus()
        self.house_number.grid(row=6, column=0, pady=(2, 10), padx=(10,5), columnspan=1)

        Label(self.frame, text="Street", fg="#fff", bg="#273C28", font=("Courier", 16, "underline")).grid(row=5, column=1,columnspan=1)
        self.street = Entry(self.frame, insertwidth=1, width=13, highlightthickness=2, highlightbackground="grey",
                                justify=CENTER, font=("Courier", 20, "normal"))
        self.street.grid(row=6, column=1, pady=(2, 10), padx=(20,5), columnspan=1)

        Label(self.frame, text="Locality", fg="#fff", bg="#273C28", font=("Courier", 16, "underline")).grid(row=5, column=2, columnspan=1)
        self.locality = Entry(self.frame, insertwidth=1, width=13, highlightthickness=2, highlightbackground="grey",
                                justify=CENTER, font=("Courier", 20, "normal"))
        self.locality.grid(row=6, column=2, pady=(2, 10), padx=(5,10), columnspan=1)

        Label(self.frame, text="City", fg="#fff", bg="#273C28", font=("Courier", 16, "underline")).grid(row=7, column=0, columnspan=1)
        self.city = Entry(self.frame, insertwidth=1, width=13, highlightthickness=2, highlightbackground="grey",
                                justify=CENTER, font=("Courier", 20, "normal"))
        self.city.grid(row=8, column=0, pady=(2, 10), padx=(10,5), columnspan=1)

        Label(self.frame, text="Pincode", fg="#fff", bg="#273C28", font=("Courier", 16, "underline")).grid(row=7, column=1, columnspan=1)
        self.pincode = Entry(self.frame, insertwidth=1, width=13, highlightthickness=2, highlightbackground="grey",
                                justify=CENTER, font=("Courier", 20, "normal"))
        self.pincode.grid(row=8, column=1, pady=(2, 10), padx=(5,5), columnspan=1)

        Label(self.frame, text="Year of construction", fg="#fff", bg="#273C28", font=("Courier", 16, "underline")).grid(row=7, column=2,columnspan=1)
        self.yoc = Entry(self.frame, insertwidth=1, width=13, highlightthickness=2, highlightbackground="grey",
                                justify=CENTER, font=("Courier", 20, "normal"))
        self.yoc.grid(row=8, column=2, pady=(2, 10), padx=(5,10), columnspan=1)

        Label(self.frame, text="Area(in sqft.)", fg="#fff", bg="#273C28", font=("Courier", 16, "underline")).grid(row=9, column=0, columnspan=1)
        self.area = Entry(self.frame, insertwidth=1, width=13, highlightthickness=2, highlightbackground="grey",
                                justify=CENTER, font=("Courier", 20, "normal"))
        self.area.grid(row=10, column=0, pady=(2, 10), padx=(10,5), columnspan=1)

        Label(self.frame, text="No. of bedrooms", fg="#fff", bg="#273C28", font=("Courier", 16, "underline")).grid(row=9, column=1, columnspan=1)
        self.bedrooms = Entry(self.frame, insertwidth=1, width=13, highlightthickness=2, highlightbackground="grey",
                                justify=CENTER, font=("Courier", 20, "normal"))
        self.bedrooms.grid(row=10, column=1, pady=(2, 10), padx=(5,5), columnspan=1)

        Label(self.frame, text="Owner's Aadhar number", fg="#fff", bg="#273C28", font=("Courier", 16, "underline")).grid(row=3, column=0, columnspan=3,pady=(5,0),padx=(25,10))
        #self.sid = Entry(self.frame, insertwidth=1, width=20, highlightthickness=2, highlightbackground="grey",
        #                        justify=CENTER, font=("Courier", 20, "normal"))
        #self.sid.grid(row=4, column=0, pady=(2, 10), padx=(20,10), columnspan=3)
        self.sid = StringVar()
        ids = list_assigned_customers("sellers")
        combobox_sid = ttk.Combobox(self.frame, textvariable=self.sid, width=30, values=ids,height=4)
        combobox_sid['state'] = 'readonly'
        combobox_sid.grid(row=4, column=0, pady=(2, 10), padx=(20,10), columnspan=3)
        type = ["Sale", "Rent", "Both"]
        self.sale_label = Label(self.frame, text="Selling Amount", fg="#fff", bg="#273C28", font=("Courier", 16, "underline"))
        self.sale_price = Entry(self.frame, insertwidth=1, width=13, highlightthickness=2, highlightbackground="grey",
                                justify=CENTER, font=("Courier", 20, "normal"))

        self.rent_label = Label(self.frame, text="Renting Amount", fg="#fff", bg="#273C28", font=("Courier", 16, "underline"))
        self.rent_price = Entry(self.frame, insertwidth=1, width=13, highlightthickness=2, highlightbackground="grey",
                                justify=CENTER, font=("Courier", 20, "normal"))
        self.availability = StringVar()
        combobox = ttk.Combobox(self.frame, textvariable=self.availability, width=10, values=type,height=2)
        combobox['state'] = 'readonly'
        combobox.grid(row=9, column=2, pady=(5, 0), padx=(0, 0),columnspan=1, rowspan=3)
        combobox.bind('<<ComboboxSelected>>', self.on_combobox_select)
        Button(self.frame, text="Add property", highlightthickness=0, width=10, height=2,
                                         highlightbackground="#273C28", font=("Courier", 15, "bold"), command=self.on_add_property_click).grid(row=13, column=0, pady=(0,0), padx=30, columnspan=3)
        Button(self.frame, text=" 🔙 ", highlightthickness=0, width=2, height=2, highlightbackground="#273C28", font=("Courier", 15, "bold"), command=self.on_back_click).grid(row=14, column=2, pady=(0, 0), columnspan=1,padx=(150,10))


    def remove_property(self):
        self.remove_button = True
        if self.add_button:
            for widgets in self.frame.grid_slaves():
                widgets.grid_forget()
            self.property_label.grid(row=0, column=0, columnspan=2, pady=(20,20), padx=20)
            self.add_radiobutton.grid(row=1, column=0, pady=(2, 10), padx=(100, 50), columnspan=1, )
            self.remove_radiobutton.grid(row=1, column=1, pady=(2, 10), padx=(50, 100), columnspan=1, )

            self.add_button = False
        self.canvas.coords(self.frame_canvas, 110, 80)
        ids = get_available_properties()

        Label(self.frame, text="Select Property:", fg="#fff", bg="#273C28", font=("Courier", 18, "bold")).grid(row=2, column=0,padx=(0,30),columnspan=2,pady=(30,5))
        self.property_remove = StringVar()
        ttk.Combobox(self.frame, textvariable=self.property_remove, width=20, values=ids).grid(row=3, column=0, pady=(5, 20), padx=(10, 10),columnspan=2)

        Button(self.frame, text="Remove", highlightthickness=0, width=10, height=2,
                                         highlightbackground="#273C28", font=("Courier", 15, "bold"),command=self.on_remove_property_click).grid(row=4, column=0, pady=(10,10), padx=30, columnspan=2)
        Button(self.frame, text=" 🔙 ", highlightthickness=0, width=2, height=2, highlightbackground="#273C28", font=("Courier", 15, "bold"), command=self.on_back_click).grid(row=5, column=1, pady=(0, 5), columnspan=1,padx=(200,20))

    def on_back_click(self):
        self.canvas.itemconfig(self.frame_canvas, window=self.old_frame, anchor="nw", )
        self.canvas.coords(self.frame_canvas, 200, 80)

    def on_combobox_select(self,event):
        self.sale_label.grid_forget()
        self.sale_price.grid_forget()
        self.rent_label.grid_forget()
        self.rent_price.grid_forget()
        if self.availability.get() == "Sale":
            self.sale_label.grid(row=11, column=0, columnspan=3)
            self.sale_price.grid(row=12, column=0, pady=(2, 10), padx=(5,5), columnspan=3)
        elif self.availability.get() == "Rent":
            self.rent_label.grid(row=11, column=0, columnspan=3)
            self.rent_price.grid(row=12, column=0, pady=(2, 10), padx=(5,5), columnspan=3)
        else:
            self.sale_label.grid(row=11, column=0, columnspan=2)
            self.sale_price.grid(row=12, column=0, pady=(2, 10), padx=(5,5), columnspan=2)
            self.rent_label.grid(row=11, column=1, columnspan=2)
            self.rent_price.grid(row=12, column=1, pady=(2, 10), padx=(5,5), columnspan=2)


    def on_add_property_click(self):
        flag = 0
        if self.house_number.get() == "" or self.street.get() == "" or self.locality.get() == "" or self.city.get() == "" or self.pincode.get() == ""or self.yoc.get() == ""or self.area.get() == ""or self.bedrooms.get() == "":
            messagebox.showwarning("Empty Entry", "Please enter all the fields.")
            flag = 1

        if len(self.pincode.get()) != 6 and flag == 0:
            messagebox.showwarning("PINCODE", "Please enter 6 digit Pincode.")
            flag = 1

        #if len(self.sid.get()) != 12 and flag == 0:
        #    messagebox.showwarning("Aadhar number", "Please enter 12 digit Aadhar number.")
        #    flag = 1

        if len(self.yoc.get()) != 4 and flag == 0:
            messagebox.showwarning("Year of construction", "Please enter 4 digit Year of construction.")
            flag = 1

        if not (self.bedrooms.get().isdigit() and self.pincode.get().isdigit() and self.area.get().isdigit()) and flag == 0:
            messagebox.showwarning("Value error", "Fill the details properly.")
            flag = 1
        
        if self.availability.get()=="" and flag==0:
            messagebox.showwarning("Enter Availability", "Please enter whether you want to sell, rent or both")
            flag = 1
        elif self.availability.get()=="Sale" and flag==0:
            if self.sale_price.get()=="" or self.sale_price.get().isnumeric()==False:
                messagebox.showwarning("Invalid/Incomplete Details", "There may be an error due to invalid details entered or details not entered.\nPlease Check")
                flag = 1
        elif self.availability.get()=="Rent" and flag==0:
            if self.rent_price.get()=="" or self.rent_price.get().isnumeric()==False:
                messagebox.showwarning("Invalid/Incomplete Details", "There may be an error due to invalid details entered or details not entered.\nPlease Check")
                flag = 1
        elif self.availability.get()=="Both" and flag==0:
            if self.sale_price.get()=="" or self.sale_price.get().isnumeric()==False or self.rent_price.get()=="" or self.rent_price.get().isnumeric()==False:
                messagebox.showwarning("Invalid/Incomplete Details", "There may be an error due to invalid details entered or details not entered.\nPlease Check")
                flag = 1

        if flag==0:
            flag = add_property(self.house_number.get(), self.street.get(), self.city.get(), self.locality.get(), self.pincode.get(),
                                self.area.get(), self.bedrooms.get(), self.yoc.get(), (self.sid.get().split(", "))[1], self.sale_price.get(),
                                self.rent_price.get(), self.availability.get())
        # check for unique id with database

        if flag == 0:
            # Add to database
            # if self.availability.get() for rent sale both
            messagebox.showinfo("Property", "Property added Successfully.")
            self.canvas.itemconfig(self.frame_canvas, window=self.old_frame, anchor="nw", )
            self.canvas.coords(self.frame_canvas, 200, 80)

    def on_remove_property_click(self):
        # self.property_remove.get() property to remove
        house_number, pincode = (self.property_remove.get()).split(", ")
        flag = remove_available_property(house_number, pincode)
        
        if flag==0:
            messagebox.showinfo("Property", "Property removed Successfully.\nAn Email has been sent to the owner for confirmation.")
            self.canvas.itemconfig(self.frame_canvas, window=self.old_frame, anchor="nw", )
            self.canvas.coords(self.frame_canvas, 200, 80)
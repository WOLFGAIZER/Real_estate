from tkinter import *
from registration import *
from tkinter import messagebox,ttk
from property import *


class Agent:
    def __init__(self, window, canvas, frame_canvas):
        self.window = window
        self.canvas = canvas
        self.frame_canvas = frame_canvas
        self.frame = Frame(window, bg="#273C28", highlightthickness=5, pady=10, padx=2, highlightbackground="grey")
        self.frame_structure()

    def frame_structure(self):
        self.main_label = Label(self.frame, text="Dashboard", bg="#273C28", borderwidth=5,
                                font=("Georgia", 30, "bold"), fg="#fff")
        self.main_label.grid(row=0, column=0, columnspan=2, pady=10, padx=20)

        self.assign_button = Button(self.frame, text="Assign", highlightthickness=0, width=15, height=2,
                                    highlightbackground="#273C28", font=("Courier", 20, "bold"), command=self.on_assign_click)
        self.assign_button.grid(row=1, column=0, pady=10, padx=30, columnspan=2)

        self.remove_button = Button(self.frame, text="Remove", highlightthickness=0, width=15, height=2,
                                    highlightbackground="#273C28", font=("Courier", 20, "bold"), command=self.on_remove_click)
        self.remove_button.grid(row=2, column=0, pady=10, padx=30, columnspan=2)

        self.property_button = Button(self.frame, text="Property", highlightthickness=0, width=15, height=2,
                                      highlightbackground="#273C28", font=("Courier", 20, "bold"), command=self.on_property_click)
        self.property_button.grid(row=3, column=0, pady=10, padx=30, columnspan=2)

        self.transaction_button = Button(self.frame, text="Transaction", highlightthickness=0, width=15, height=2,
                                         highlightbackground="#273C28", font=("Courier", 20, "bold"), command=self.on_transaction_click)
        self.transaction_button.grid(row=4, column=0, pady=10, padx=30, columnspan=2)

    def on_assign_click(self):
        register = Registration("Customer",self.window,self.canvas,self.frame,self.frame_canvas, None)
        self.canvas.itemconfig(self.frame_canvas, window=register.frame, anchor="nw", )
        self.canvas.coords(self.frame_canvas, 70, 40)

    def on_remove_click(self):

        def drop_down_list():
            combobox["values"] = list_assigned_customers(self.radio_value.get())

        def on_deactivate_click():
            # deactivation_id.get() remove from respective database
            flag = unassign_customer(self.radio_value.get(), (deactivation_id.get()).split(", ")[1])
            if flag==0:
                messagebox.showinfo("Removal Successful", f"{(deactivation_id.get()).split()[0]} has been unassigned from you. An email has been sent to the customer for confirmation.")
                self.canvas.itemconfig(self.frame_canvas, window=self.frame, anchor="nw", )
                self.canvas.coords(self.frame_canvas, 200, 80)

        frame = Frame(self.window, bg="#273C28", highlightthickness=2, pady=10, padx=2, highlightbackground="grey", borderwidth=5)
        self.canvas.itemconfig(self.frame_canvas, window=frame, anchor="nw", )
        self.canvas.coords(self.frame_canvas, 110, 110)
        Label(frame, text="Account Deactivation", bg="#273C28", borderwidth=5, font=("Georgia", 30, "bold"),
                               fg="#fff").grid(row=0, column=0, columnspan=2, pady=(20,30), padx=20)
        self.radio_value = StringVar(value="buyers")
        Radiobutton(frame, text="Owner", variable=self.radio_value, value="sellers", bg="#273C28", fg="#fff", command=drop_down_list).grid( row=1, column=0, pady=(2, 10), padx=(140, 10))
        Radiobutton(frame, text="Purchaser", variable=self.radio_value, value="buyers", bg="#273C28", fg="#fff", command=drop_down_list).grid(row=1, column=1, pady=(2, 10), padx=(10, 100))
        # check radio_value then put buyer or seller ids in list
        # self.ids = list_assigned_customers(self.radio_value.get())

        deactivation_id = StringVar(value="Select Aadhar number")
        # OptionMenu(frame, deactivation_id, *ids).grid(row=2, column=0, pady=(20, 20), padx=(10, 10),columnspan=2)
        combobox = ttk.Combobox(frame, textvariable=deactivation_id, width=40)
        combobox.grid(row=2, column=0, pady=(20, 20), padx=(10, 10),columnspan=2)
        drop_down_list()
        Button(frame, text="Deactivate", highlightthickness=0, width=10, height=2,
                                         highlightbackground="#273C28", font=("Courier", 15, "bold"), command=on_deactivate_click).grid(row=3, column=0, pady=(10,10), padx=30, columnspan=2)
        Button(frame, text=" 🔙 ", highlightthickness=0, width=2, height=2, highlightbackground="#273C28", font=("Courier", 15, "bold"), command=self.on_back_click).grid(row=11, column=1, pady=(0, 5), columnspan=1,padx=(200,20))

    def on_property_click(self):
        property = Property(self.window, self.canvas, self.frame_canvas, self.frame)
        self.canvas.itemconfig(self.frame_canvas, window=property.frame, anchor="nw", )

    def on_transaction_click(self):
        def on_dot_click(event):
            if self.dot.get() == "yyyy-mm-dd":
                self.dot.delete(0, "end")
                self.dot.config(foreground="#000000")

        def on_record_click():
            # get everything
            flag = 0
            if self.dot.get() == "" or self.price.get() == "":
                messagebox.showwarning("Empty Entry", "Please enter all the fields.")
                flag = 1

            if not (self.price.get().isdigit()) and flag == 0:
                messagebox.showwarning("Value error", "Fill the details properly.")
                flag = 1
            
            if len(self.dot.get())!=10 and flag == 0:
                messagebox.showwarning("Invalid Date Entry", "Please enter the date in correct format (yyyy-mm-dd)\nInclude the hyphens as well")
                flag = 1
            elif flag==0:
                if self.dot.get()[4]!='-' or self.dot.get()[7]!='-' or self.dot.get()[:4].isdigit()==False or self.dot.get()[5:7].isdigit()==False or self.dot.get()[8:].isdigit()==False:
                    messagebox.showwarning("Invalid Date Entry", "Please enter the date in correct format (yyyy-mm-dd)\nInclude the hyphens as well")
                    flag = 1
            
            if flag==0:
                flag = perform_transaction(buyer_id.get().split(", ")[1], seller_id.get().split(", ")[1], property.get().split(", ")[0], property.get().split(", ")[1], self.dot.get(), self.price.get(), self.radio_value.get())
            
            if flag == 0:
                messagebox.showinfo("Transaction", "Transaction recorded successfully.")
                self.canvas.itemconfig(self.frame_canvas, window=self.frame, anchor="nw", )
                self.canvas.coords(self.frame_canvas, 200, 80)

        frame = Frame(self.window, bg="#273C28", highlightthickness=2, pady=10, padx=2, highlightbackground="grey", borderwidth=5)
        self.canvas.itemconfig(self.frame_canvas, window=frame, anchor="nw", )
        self.canvas.coords(self.frame_canvas, 80, 40)
        buyer_ids = list_assigned_customers("buyers") ##Obtain IDs
        seller_ids = list_assigned_customers("sellers")
        properties = get_available_properties()
        Label(frame, text="Transaction Record", bg="#273C28", borderwidth=5, font=("Georgia", 30, "bold"),
                               fg="#fff").grid(row=0, column=0, columnspan=3, pady=(20,10), padx=20)

        Label(frame, text="Purchaser's id:", fg="#fff", bg="#273C28", font=("Courier", 18, "bold")).grid(row=1, column=0,padx=(0,30))
        buyer_id = StringVar()
        ttk.Combobox(frame, textvariable=buyer_id,height= 3, width=30, values=buyer_ids, font=("Courier", 12, "bold")).grid(row=1, column=1, pady=(10, 10), padx=(10, 10),columnspan=2)

        Label(frame, text="Owner's id:", fg="#fff", bg="#273C28", font=("Courier", 18, "bold")).grid(row=2, column=0,padx=(0,30))
        seller_id = StringVar()
        ttk.Combobox(frame, textvariable=seller_id,height= 3, width=30, values=seller_ids, font=("Courier", 12, "bold")).grid(row=2, column=1, pady=(10, 10), padx=(10, 10),columnspan=2)

        Label(frame, text="Select Property:", fg="#fff", bg="#273C28", font=("Courier", 18, "bold")).grid(row=3, column=0,padx=(0,30))
        property = StringVar()
        ttk.Combobox(frame, textvariable=property,height=3, width=30, values=properties, font=("Courier", 12, "bold")).grid(row=3, column=1, pady=(10, 10), padx=(10, 10),columnspan=2)

        Label(frame, text="Date of Transaction:", fg="#fff", bg="#273C28", font=("Courier", 18, "bold")).grid(row=4, column=0,padx=(20,30))
        self.dot = Entry(frame, insertwidth=1, width=15, foreground="#d3d3d3", highlightthickness=2, highlightbackground="grey", justify=CENTER, font=("Courier", 20, "normal"))
        self.dot.focus()
        self.dot.bind("<Button-1>", on_dot_click)
        self.dot.insert(0, "yyyy-mm-dd")
        self.dot.grid(row=4, column=1,pady=10)

        Label(frame, text="Price: ", fg="#fff", bg="#273C28", font=("Courier", 18, "bold")).grid(row=5, column=0,padx=(0,30))
        self.price = Entry(frame, insertwidth=1, width=15, highlightthickness=2, highlightbackground="grey", justify=CENTER, font=("Courier", 20, "normal"))
        self.price.grid(row=5, column=1,pady=(10,20))

        self.radio_value = StringVar(value="RENT")
        Radiobutton(frame, text="Rent", variable=self.radio_value, value="RENT", bg="#273C28", fg="#fff", font= ("Courier", 18, "normal")).grid(row=6, column=0,pady=(2, 10),padx=(80, 20))
        Radiobutton(frame, text="Sale", variable=self.radio_value, value="SOLD", bg="#273C28", fg="#fff", font= ("Courier", 18, "normal")).grid(row=6,column=1,pady=(2, 10),padx=(20, 80))
        Button(frame, text="Record", highlightthickness=0, width=10, height=2,
                                         highlightbackground="#273C28", font=("Courier", 15, "bold"), command=on_record_click).grid(row=7, column=0, pady=(5,5), padx=30, columnspan=2)
        Button(frame, text=" 🔙 ", highlightthickness=0, width=2, height=2, highlightbackground="#273C28", font=("Courier", 15, "bold"), command=self.on_back_click).grid(row=8, column=1, pady=(0, 5), columnspan=1,padx=(200,20))

    def on_back_click(self):
        self.canvas.itemconfig(self.frame_canvas, window=self.frame, anchor="nw", )
        self.canvas.coords(self.frame_canvas, 200, 80)






from tkinter import *
from tkinter import ttk
from database import *


def agent_frame(type):
    def on_back_click():
        canvas.itemconfig(frame_canvas, window=frame, anchor="nw", )

    def on_fetch_click():
        def on_back_click_inside():
            canvas.itemconfig(frame_canvas, window=agents_frame, anchor="nw", )
            canvas.config(width=720, height=560)
            bg = canvas.create_image(360, 280, image=bg_image)
            canvas.coords(frame_canvas, 150, 100)
            window.geometry("720x560+400+150")

        if type == "Sale":
            report = get_sale_report(agent_id.get())
            report_frame = Frame(window, bg="#273C28", highlightthickness=5, pady=20, padx=20,highlightbackground="grey")
            if report:
                columns = ('house_number', 'street', 'locality', 'city', 'price', 'transaction_date')

                tree = ttk.Treeview(report_frame, columns=columns, show='headings')
                tree.heading('house_number', text='house_number')
                tree.heading('street', text='street')
                tree.heading('locality', text='locality')
                tree.heading('city', text='city')
                tree.heading('price', text='price')
                tree.heading('transaction_date', text='transaction_date')
                for details in report:
                    tree.insert('', END, values=details)
                tree.grid(row=0, column=0, sticky='nsew')
            else:
                Label(report_frame, text="No Property Sold", bg="#273C28", borderwidth=5, font=("Georgia", 30, "bold"),
                      fg="#fff").grid(row=0, column=0, columnspan=2, pady=(20, 30), padx=20)

        else:
            report = get_rent_report(agent_id.get())
            report_frame = Frame(window, bg="#273C28", highlightthickness=5, pady=20, padx=20, highlightbackground="grey")
            columns = ('house_number', 'street', 'locality', 'city', 'price', 'transaction_date')

            tree = ttk.Treeview(report_frame, columns=columns, show='headings')
            tree.heading('house_number', text='house_number')
            tree.heading('street', text='street')
            tree.heading('locality', text='locality')
            tree.heading('city', text='city')
            tree.heading('price', text='price')
            tree.heading('transaction_date', text='transaction_date')
            if report:
                for details in report:
                    tree.insert('', END, values=details)
                tree.grid(row=0, column=0, sticky='nsew')
            else:
                Label(report_frame, text="No Property Rented", bg="#273C28", borderwidth=5, font=("Georgia", 30, "bold"),
                      fg="#fff").grid(row=0, column=0, columnspan=2, pady=(20, 30), padx=20)

        if report:
            canvas.config(width=1440, height=1120)
            # canvas.itemconfig(bg, image=image_bg)
            bg_change = canvas.create_image(720, 560, image=image_bg)
            window.geometry("1300x650+200+150")
            canvas.coords(frame_canvas, 20, 100)
        else:
            canvas.coords(frame_canvas, 150, 150)

        Button(report_frame, text=" 🔙 ", highlightthickness=0, width=2, height=2, highlightbackground="#273C28",
               font=("Courier", 15, "bold"), command=on_back_click_inside).grid(row=20, column=0, pady=(20, 5), columnspan=2, padx=(0, 0))
        canvas.itemconfig(frame_canvas, window=report_frame, anchor="nw", )
    agents_frame = Frame(window, bg="#273C28", highlightthickness=5, pady=20, padx=20, highlightbackground="grey")
    Label(agents_frame, text="Select Agent ID :", bg="#273C28", borderwidth=5, font=("Georgia", 30, "bold"),
          fg="#fff").grid(row=0, column=0, columnspan=2, pady=(20, 30), padx=20)
    agent_id = StringVar()
    ids = get_agent_ids()
    ttk.Combobox(agents_frame, textvariable=agent_id, width=15, values=ids).grid(row=1, column=0, pady=(20, 20), padx=(10, 10), columnspan=2)
    Button(agents_frame, text="Fetch report", highlightthickness=0, width=13, height=2,
           highlightbackground="#273C28", font=("Courier", 20, "bold"), command=on_fetch_click).grid(row=2, column=0, pady=(10, 15), padx=30, columnspan=2)
    Button(agents_frame, text=" 🔙 ", highlightthickness=0, width=2, height=2, highlightbackground="#273C28",
           font=("Courier", 15, "bold"), command=on_back_click).grid(row=3, column=1, pady=(20, 5), columnspan=1, padx=(200, 0))

    canvas.itemconfig(frame_canvas, window=agents_frame, anchor="nw", )

def on_sale_click():
    agent_frame("Sale")

def on_rent_click():
    agent_frame("Rent")

window = Tk()
window.title("Real Estate Agency")
window.config(bg="#000")
window.geometry("720x560+400+150")

bg_image = PhotoImage(file="Matrix Real estate1.png")

canvas = Canvas(width=720, height=560, highlightthickness=0)
bg = canvas.create_image(360, 280, image=bg_image)
image_bg = bg_image.zoom(2, 2)

frame = Frame(window, bg="#273C28", highlightthickness=5, pady=20, padx=20, highlightbackground="grey")
frame_canvas = canvas.create_window(150, 100, window=frame, anchor="nw", )
login_label = Label(frame, text="Matrix Real Estate", bg="#273C28",borderwidth=5, font=("Georgia",35,"bold"), fg="#fff")
login_label.grid(row=0, column=0, columnspan=2, pady=10)

Button(frame, text="Sale report", highlightthickness=0, width=15, height=2,
                            highlightbackground="#273C28", font=("Courier", 20, "bold"), command=on_sale_click).grid(row=1, column=0, pady=(30,15), padx=30, columnspan=2)

Button(frame, text="Rent Report", highlightthickness=0, width=15, height=2,
                            highlightbackground="#273C28", font=("Courier", 20, "bold"), command=on_rent_click).grid(row=2, column=0, pady=(10,20), padx=30, columnspan=2)

canvas.grid(column=0, row=0)


window.mainloop()

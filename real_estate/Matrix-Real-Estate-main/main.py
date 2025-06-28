from tkinter import *
from registration import *
from agent import *
from database import *

def on_username_click(event):
    if username_entry.get() == "Username":
        username_entry.delete(0, "end")
        username_entry.config(foreground="#000000")


def on_password_click(event):
    if password_entry.get() == "Password":
        password_entry.delete(0, "end")
        password_entry.config(foreground="#000000")



def on_sign_up_click():
    agent_register = Registration("agent", window=window, canvas=canvas, old_frame=login_frame,frame_canvas=login_canvas, background = bg)
    canvas.itemconfig(bg, image=next_page_bg)
    # login_frame.destroy()
    # reg_canvas = canvas.create_window(60, 60, window=agent_register.frame, anchor="nw")
    # canvas.update_idletasks()
    canvas.itemconfig(login_canvas, window=agent_register.frame, anchor="nw", )
    canvas.coords(login_canvas, 40, 20)
    # canvas.delete(login_canvas)
    # canvas.itemconfig(bg, image=next_page_bg)
    # reg_canvas = canvas.create_window(60, 60, window=agent_register.frame, anchor="nw", )

def on_login_click():
    flag = 0
    global username, password
    username = username_entry.get()
    password = password_entry.get()

    if username == '' or username == 'Username':
        messagebox.showinfo("Invalid Details", "Please enter Username")
        return
    if password=='' or password == 'Password':
        messagebox.showinfo("Invalid Details", "Please enter Password")
        return    

    flag, message, agent_info = login_agent(username, password)

    if flag==1:
        messagebox.showwarning("Login Error", message)

    # if username_entry.get() not in database or password_entry.get() does not match in database:
    #     messagebox.showwarning("Login Error", "Username or Password is invalid.")
    #     flag =1

    if flag == 0:
        messagebox.showinfo("Login Successful", f"Welcome Back {agent_info[1].split()[0]}!")
        canvas.itemconfig(bg, image=next_page_bg)
        login_frame.destroy()
        agent = Agent(window=window,canvas=canvas,frame_canvas=login_canvas)
        agent_canvas = canvas.create_window(200, 80, window=agent.frame, anchor="nw")
        agent.frame_canvas = agent_canvas


window = Tk()
window.title("Real Estate Agency")
window.config(bg="#000")
window.geometry("720x560+400+150")

front_page_bg = PhotoImage(file="Matrix Real estate.png")
next_page_bg = PhotoImage(file="Matrix Real estate1.png")

canvas = Canvas(width=720, height=560, highlightthickness=0)
bg = canvas.create_image(360, 280, image=front_page_bg)


login_frame = Frame(window, bg="#273C28", highlightthickness=5, pady=10, padx=2, highlightbackground="grey")
login_canvas = canvas.create_window(120, 60, window=login_frame, anchor="nw", )
login_label = Label(login_frame, text="SIGN IN", bg="#273C28",borderwidth=5, font=("Georgia",35,"bold"), fg="#fff")
login_label.grid(row=0, column=0, columnspan=2, pady=10)

canvas.grid(column=0, row=0)

username_entry = Entry(login_frame, insertwidth=1, foreground="#d3d3d3", width=20,highlightthickness=2, highlightbackground="grey",justify=CENTER,font=("Courier",20,"normal"))
username_entry.insert(0, "Username")
username_entry.bind("<Button-1>", on_username_click)
username_entry.grid(row=1, column=0, columnspan=2, pady=5, padx=10)

password_entry = Entry(login_frame, show="*", insertwidth=1, foreground="#d3d3d3", width=20,highlightthickness=2, highlightbackground="grey",justify=CENTER,font=("Courier",20,"normal"))
password_entry.insert(0, "Password")
password_entry.bind("<Button-1>", on_password_click)
password_entry.grid(row=2, column=0, columnspan=2, pady=5, padx=10)


login_button = Button(login_frame, text="Login", highlightthickness=0, width=17, height=2, highlightbackground="#273C28",font=("Courier", 17, "bold"), command=on_login_click)
login_button.grid(row=3, column=0, columnspan=2, pady=(10, 20))

register_label = Label(login_frame, text="Don't have an account?",fg="#fff",bg="#273C28",font=("Courier", 16, "underline"))
register_label.grid(row=4, column=0, pady=(0, 10), columnspan=1, padx=(60, 0))

sign_up_button = Button(login_frame, text="Sign Up", highlightthickness=0, width=10, height=1, highlightbackground="#273C28", command=on_sign_up_click)
sign_up_button.grid(row=4, column=1, pady=(0, 13), columnspan=1, padx=(0,60))


window.mainloop()

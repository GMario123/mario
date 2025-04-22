import tkinter as tk

window = tk.Tk()
window.title("hello")
window.geometry("500x300")


l1 = tk.Label(window,text="User Name")
l1.pack()
u_name= tk.stringVar()
t1 = tk.Entry(window,textvariable=u_name)
t1.pack()
l2 = tk. Label(window ,text="password")
l2.pack()
u_pwd = tk.StringVar()
l2=tk.Label(window,textvariable=u_pwd)
t1.pack()
def chk_cred():
    if u_name.get()=="Ananya" and u_pwd.get()=="ann":
        messagebox.showinfo(window,"Login successful!!!")
    else:
        messagebox.showinfo(window,"Wrong credential:(")
       

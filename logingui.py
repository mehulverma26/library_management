from maingui import *
from datetime import datetime
import pytz
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pandas as pd
empleey=pd.read_csv("empleey.csv")
def check():
    c=True
    cid=e.get()
    i=0
    try:
        while c:
            if empleey.xs(i)['Empleey ID']== cid:
                cid=i
                c=False
            else:
                i=+1
    except:
        messagebox.showerror("error","incorrect Id")
        e.delete(0,len(e.get()))
        e1.delete(0,len(e1.get()))
    try:
        if empleey.xs(cid)["passcode"]==e1.get():
            messagebox.showinfo("Wellcome",empleey.xs(cid)["Empleey Name"])
            root.destroy()
            function(empleey.xs(cid)["Empleey Name"])
            
        else:
            messagebox.showerror("error","incorrect passcode")
            e.delete(0,len(e.get()))
            e1.delete(0,len(e1.get()))
    except:
        pass
def fop ():
    def ch1():
        global id
        id=admin.get()
        try:
            i=empleey[empleey['Empleey ID']==id].index.values
            i=i[0]
            lab.configure(text="New Passcode")
            but.configure(command=ch2)
            admin.delete(0,len(admin.get()))
            id=i
        except:
            messagebox.showerror("error","incorrect Id")
            admin.delete(0,len(admin.get()))
    def ch2():
        global id
        empleey.loc[id,"passcode"]=admin.get()
        empleey.to_csv("empleey.csv",index=False)
        root1.destroy()
    def ch():
        if admin.get()=="2004":
            lab.configure(text="User ID")
            admin.delete(0,len(admin.get()))
            but.configure(command=ch1)
        else:
            messagebox.showerror("Error","Incorrect Admin PIN")
            admin.delete(0,len(admin.get()))
    root1=Tk()
    root1.geometry("300x150")
    root1.title("Passcode Reseat")
    root1.resizable(0,0)
    f12=Frame(root1)
    f12.pack(expand=True,fill=BOTH)
    f2=Frame(root1,bg="silver")
    f2.pack(expand=True,fill=BOTH)
    f3=Frame(root1,bg="silver")
    f3.pack(expand=True,fill=BOTH)
    lab=Label(f12,text="Admin pin",font=("FrankRuehl",20),bg="silver",justify=CENTER)
    lab.pack(expand=True,fill=BOTH)
    admin=Entry(f2,width=30,justify=CENTER)
    admin.pack()
    but=Button(f3,text="Enter",font=("FrankRuehl",15),bg="white",command=ch,justify=CENTER)
    but.pack()
def be(event):
    bn.configure(bg="black",fg="white",image=photoimage4)
def bl(event):
    bn.configure(bg="white",fg="black",image=photoimage3)
def fe(event):
    fp.configure(fg="blue")
def fl(event):
    fp.configure(fg="black")
root=Tk()
root.geometry("1199x600+100+50")
root.title("Library Management System")
logo=PhotoImage(file=r"lo.png")
root.iconphoto(False,logo)
root.resizable(0,0)
photo4 = PhotoImage(file = r"login-512.png")
photoimage4 = photo4.subsample(20,20)
photo3 = PhotoImage(file = r"login.png")
photoimage3 = photo3.subsample(20,20)
photo2 = PhotoImage(file = r"logo1.png")
photoimage2 = photo2.subsample(1,1)
photo1 = PhotoImage(file = r"lg2.png")
photoimage1 = photo1.subsample(33,33)
photo = PhotoImage(file = r"lg.png")
photoimage = photo.subsample(18,18)
image = Image.open(r"bg.png")
image = image.resize((1300, 650), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(image)
backg = Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
box=Frame(root,bg="silver")
box.place(x=350,y=140,width=500,height=340)
titel=Label(box,text="Library Management",image=photoimage2,font=("FrankRuehl",35,"bold"),compound=LEFT,fg="black",bg="silver").place(x=0,y=30)
l = Label(box,text="User ID:",image=photoimage, font=("FrankRuehl",20),fg="black",bg="silver",compound=LEFT).place(x=0,y=130)
e= Entry(box, width=50)
e.place(x=150,y=135)
l1= Label(box, text="Passcode:",image=photoimage1, font=("FrankRuehl",20),fg="black",bg="silver",compound=LEFT).place(x=0,y=180)
e1= Entry(box, show='*', width=50)
e1.place(x=150,y=185)
bn=Button(box,text="Login",font=("FrankRuehl",20),command=check,bg="white",image=photoimage3,compound=LEFT)
bn.place(x=200,y=220)
fp=Button(box,text="Forgote Password",font=("FrankRuehl",10,"underline"),command=fop,bg="silver",bd=0)
fp.place(x=195,y=270)
fp.bind("<Enter>",fe)
fp.bind("<Leave>",fl)
bn.bind("<Enter>",be)
bn.bind("<Leave>",bl)
root.mainloop()
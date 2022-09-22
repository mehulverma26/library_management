from main import *
from tkinter import *
from datetime import datetime
import pytz
from PIL import ImageTk, Image
def function(id):
    global lbl
    root1=Tk()
    root1.geometry("800x650")
    root1.title("Library Management")
    logo=PhotoImage(file=r"lo.png")
    root1.iconphoto(False,logo)
    root1.resizable(0,0)
    ######################################################################################################################
    def abe(event):
        ab.configure(bg="black",fg="white")
    def abl(event):
        ab.configure(bg="#CCFFFF",fg="black")
    def ibe(event):
        ib.configure(bg="black",fg="white")
    def ibl(event):
        ib.configure(bg="#CCFFFF",fg="black")
    def lbe(event):
        lb.configure(bg="black",fg="white")
    def lble(event):
        lb.configure(bg="#CCFFFF",fg="black")
    def rbe(event):
        rb.configure(bg="black",fg="white")
    def rbl(event):
        rb.configure(bg="#CCFFFF",fg="black")
    def dbe(event):
        db.configure(bg="black",fg="white")
    def dbl(event):
        db.configure(bg="#CCFFFF",fg="black")
    def sbe(event):
        sb.configure(bg="black",fg="white")
    def sbl(event):
        sb.configure(bg="#CCFFFF",fg="black")
    ######################################################################################################################
    image1 = Image.open(r"ab.png")
    photoimageab = ImageTk.PhotoImage(image1)
    image2 = Image.open(r"c.png")
    photoimagesb = ImageTk.PhotoImage(image2)
    image3 = Image.open(r"i.png")
    photoimageib = ImageTk.PhotoImage(image3)
    image4 = Image.open(r"r.png")
    photoimagerb = ImageTk.PhotoImage(image4)
    image5 = Image.open(r"d.png")
    photoimagedb = ImageTk.PhotoImage(image5)
    image6 = Image.open(r"l.png")
    photoimagelb = ImageTk.PhotoImage(image6)
    image = Image.open(r"bg.png")
    photo = PhotoImage(file = r"log.png")
    photoimage = photo.subsample(1,1)
    photo1 = PhotoImage(file = r"u.png")
    photoimage1 = photo1.subsample(30,30)
    image = image.resize((850, 550), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(image)
    ######################################################################################################################
    frame1=Frame(root1,bg="silver",height=120,width=1000)
    frame1.pack(expand=False,fill=None)
    frame2=Frame(root1,bg="white",height=40,width=1000)
    frame2.pack(expand=False,fill=None)
    frame3=Label(root1,image=bg)
    frame3.pack(expand=TRUE,fill=BOTH)
    ######################################################################################################################
    ab=Button(frame3,image=photoimageab,compound=LEFT,text="Add Book",font=("FrankRuehl",20,"bold"),height=70,width=230,bg="#CCFFFF",command=addbook)
    ab.place(x=80,y=50)
    sb=Button(frame3,image=photoimagesb,compound=LEFT,text="Search Book",font=("FrankRuehl",20,"bold"),height=70,width=230,bg="#CCFFFF",command=checkbook)
    sb.place(x=470,y=50)
    ib=Button(frame3,image=photoimageib,compound=LEFT,text="Issue Book",font=("FrankRuehl",20,"bold"),height=70,width=230,bg="#CCFFFF",command=issuethebook)
    ib.place(x=80,y=200)
    rb=Button(frame3,image=photoimagerb,compound=LEFT,text="Return Book",font=("FrankRuehl",20,"bold"),height=70,width=230,bg="#CCFFFF",command=returnfunction)
    rb.place(x=470,y=200)
    db=Button(frame3,image=photoimagedb,compound=LEFT,text="Delete Book",font=("FrankRuehl",20,"bold"),height=70,width=230,bg="#CCFFFF",command=deletebook)
    db.place(x=80,y=350)
    lb=Button(frame3,image=photoimagelb,compound=LEFT,text="Show Books",font=("FrankRuehl",20,"bold"),height=70,width=230,bg="#CCFFFF",command=listbooks)
    lb.place(x=470,y=350)
    ######################################################################################################################
    l1=Label(frame1,image=photoimage,text="Library Management",bg="silver",font=("FrankRuehl",50,"bold"),compound=LEFT)
    l1.place(x=60,y=25)
    l2=Label(frame2,image=photoimage1,text=id,bg="white",font=("FrankRuehl",15,"bold"),compound=LEFT)
    l2.place(x=4,y=0)
    lbl = Label(frame2, font = ('FrankRuehl', 15, 'bold'), background = 'white')
    lbl.place(x=645,y=10)
    def time():
        global lbl
        world=pytz.timezone("Asia/kolkata")
        datetime_India=datetime.now(world)
        timee=datetime_India.strftime("%H:%M:%S")
        sring = timee
        lbl.config(text=f"Time:->{sring}")
        lbl.after(1000, time)
    time()
    ######################################################################################################################
    ab.bind("<Enter>",abe)
    ab.bind("<Leave>",abl)
    db.bind("<Enter>",dbe)
    db.bind("<Leave>",dbl)
    rb.bind("<Enter>",rbe)
    rb.bind("<Leave>",rbl)
    ib.bind("<Enter>",ibe)
    ib.bind("<Leave>",ibl)
    lb.bind("<Enter>",lbe)
    lb.bind("<Leave>",lble)
    sb.bind("<Enter>",sbe)
    sb.bind("<Leave>",sbl)
    root1.mainloop()
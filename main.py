from tkinter import *
from tkinter import messagebox
from datetime import *
import pandas as pd

def issuethebook():
    def enter(n):
        book=pd.read_csv("Book.csv")
        student=pd.read_csv("student.csv")
        issued=pd.read_csv("issued.csv")    
        try:
            j=book[book["Book ID"]==d.get()].index.values
            j=j[0]
            if book.xs(j)["Avalibility"]=="available":
                datee=datetime.now().timetuple().tm_yday
                tempissu=pd.DataFrame({"Student ID":student.xs(n)["Student ID"],"Student Name":student.xs(n)['Student Name'],"Book ID":d.get(),"Day of issu":datee},index=[0])
                issued=issued.append(tempissu,ignore_index=True)
                issued.to_csv("issued.csv",index=False)
                book.loc[j,"Avalibility"]="Unavilable"
                book.to_csv("Book.csv",index=False)
                messagebox.showinfo("sucess","Book issued sucessfully")
                root2.destroy()
            else:
                messagebox.showwarning("Warning","all read issued to someone")
        except:
            messagebox.showerror("Error","no book existi of this id")
    def enter1():
        student=pd.read_csv("student.csv")
        try:
            j=(student[student["Student ID"]==d.get()].index.values)
            idl.configure(text="Book ID")
            j=j[0]
            en.configure(command=lambda:enter(j))
            d.delete(0,len(d.get()))
        except:
            messagebox.showerror("Not Registerd","student not registerd in data base can't issue book")
            d.delete(0,len(d.get()))
    root2=Tk()
    root2.title("Issue Book")
    root2.geometry("300x300")
    root2.resizable(0,0)
    f1=Frame(root2,background="#CCFFFF")
    f1.pack(expand=True,fill=BOTH)
    f2=Frame(root2,background="#CCFFFF")
    f2.pack(expand=True,fill=BOTH)
    f3=Frame(root2,background="#CCFFFF")
    f3.pack(expand=True,fill=BOTH)
    idl=Label(f1,text="Student ID",justify=LEFT,bg="#CCFFFF",font=("FrankRuehl",20,"bold"))
    idl.pack(expand=True,fill=BOTH)
    d=Entry(f2,width=30)
    d.pack()
    en=Button(f3,text="Enter",justify=LEFT,bg="#CCFFFF",font=("FrankRuehl",20,"bold"),command=enter1)
    en.pack()
    root2.mainloop()

def returnfunction():
    def enter():
        book=pd.read_csv("Book.csv")
        issued=pd.read_csv("issued.csv")
        try:
            k=issued[issued["Student ID"]==d.get()].index.values
            s=k[0]
            cdatee=datetime.now().timetuple().tm_yday
            pdatee=issued.xs(s)["Day of issu"]
            charge=cdatee-pdatee
            if charge==0:
                pass
            else:
                fine=charge*5
                messagebox.showinfo("Fin",f"Take Rs. {fine} for late returning")
            cid=issued.xs(s)["Book ID"]
            cid=book[book["Book ID"]==cid].index.values
            cid=cid[0]
            book.loc[cid,"Avalibility"]="available"
            book.to_csv("Book.csv",index=False)
            issued=issued.drop(index=s)
            issued.to_csv("issued.csv",index=False)
            messagebox.showinfo("sucess","Returend sucessfully")
            root2.destroy()
        except:
            messagebox.showinfo("","dont have any book issued")
            root2.destroy()
    root2=Tk()
    root2.title("Returan Book")
    root2.geometry("300x300")
    root2.resizable(0,0)
    f1=Frame(root2,background="#CCFFFF")
    f1.pack(expand=True,fill=BOTH)
    f2=Frame(root2,background="#CCFFFF")
    f2.pack(expand=True,fill=BOTH)
    f3=Frame(root2,background="#CCFFFF")
    f3.pack(expand=True,fill=BOTH)
    idl=Label(f1,text="Student ID",justify=LEFT,bg="#CCFFFF",font=("FrankRuehl",20,"bold"))
    idl.pack(expand=True,fill=BOTH)
    d=Entry(f2,width=30)
    d.pack()
    en=Button(f3,text="Enter",justify=LEFT,bg="#CCFFFF",font=("FrankRuehl",20,"bold"),command=enter)
    en.pack()
    root2.mainloop()

def checkbook():
    book=pd.read_csv("Book.csv")
    def enter():
        cid=d.get()
        try:
            id=(book[book["Book ID"]==cid].index.values)
            id=id[0]
            d.delete(0,len(d.get()))
            root4=Tk()
            root4.title("Book details")
            root3=Frame(root4,bg="#CCFFFF")
            root3.pack(expand=True,fill=BOTH)
            l11=Label(root3,text="Book ID",bg="#CCFFFF",font=("FrankRuehl",20,"bold"),justify=LEFT).grid(column=0,row=0)
            l12=Label(root3,text="Book Name",bg="#CCFFFF",font=("FrankRuehl",20,"bold"),justify=LEFT).grid(column=0,row=1)
            l13=Label(root3,text="Author",bg="#CCFFFF",font=("FrankRuehl",20,"bold"),justify=LEFT).grid(column=0,row=2)
            l14=Label(root3,text="Edition",bg="#CCFFFF",font=("FrankRuehl",20,"bold"),justify=LEFT).grid(column=0,row=3)
            l15=Label(root3,text="Avalibility",bg="#CCFFFF",font=("FrankRuehl",20,"bold"),justify=LEFT).grid(column=0,row=4)
            l1=Label(root3,text=(book.xs(id)["Book ID"]),bg="#CCFFFF",font=("FrankRuehl",20,"bold"),justify=LEFT).grid(column=1,row=0)
            l2=Label(root3,text=(book.xs(id)["Book Name"]),bg="#CCFFFF",font=("FrankRuehl",20,"bold"),justify=LEFT).grid(column=1,row=1)
            l3=Label(root3,text=(book.xs(id)["Author"]),bg="#CCFFFF",font=("FrankRuehl",20,"bold"),justify=LEFT).grid(column=1,row=2)
            l4=Label(root3,text=(book.xs(id)["Edition"]),bg="#CCFFFF",font=("FrankRuehl",20,"bold"),justify=LEFT).grid(column=1,row=3)
            l5=Label(root3,text=(book.xs(id)["Avalibility"]),bg="#CCFFFF",font=("FrankRuehl",20,"bold"),justify=LEFT).grid(column=1,row=4)
            root4.mainloop()
        except:
            messagebox.showerror("Error","no book existi of this id")
            d.delete(0,len(d.get()))
    root2=Tk()
    root2.title("Search Book")
    root2.geometry("200x100")
    root2.resizable(0,0)
    f2=Frame(root2,background="#CCFFFF")
    f2.pack(expand=True,fill=BOTH)
    f3=Frame(root2,background="#CCFFFF")
    f3.pack(expand=True,fill=BOTH)
    idl=Label(f2,text="Book ID",justify=LEFT,bg="#CCFFFF",font=("FrankRuehl",20,"bold")).grid(column=0,row=0)
    d=Entry(f2,width=10)
    d.grid(column=1,row=0)
    en=Button(f3,text="Enter",justify=LEFT,bg="#CCFFFF",font=("FrankRuehl",20,"bold"),command=enter).pack()
    root2.mainloop()

def deletebook():
    def enter():
        book=pd.read_csv("Book.csv")
        try:
            id=d.get()
            j=(book[book["Book ID"]==id].index.values)
            m=book.loc[j]
            a=messagebox.askquestion("Aleart",f"Are you sure you want to delete following data:->\n{m}")
            if a=="yes":
                messagebox.showinfo("Sucessful","Book Deleted Sucessfully")
                d.delete(0,len(d.get()))
                book=book.drop(index=j)
                book.to_csv("Book.csv",index=False)
            else:
                d.delete(0,len(d.get()))
                pass
        except:
            messagebox.showerror("error","no book existi of this id")
            d.delete(0,len(d.get()))
    root2=Tk()
    root2.title("Delete Book")
    root2.geometry("200x100")
    root2.resizable(0,0)
    f2=Frame(root2,background="#CCFFFF")
    f2.pack(expand=True,fill=BOTH)
    f3=Frame(root2,background="#CCFFFF")
    f3.pack(expand=True,fill=BOTH)
    idl=Label(f2,text="Book ID",justify=LEFT,bg="#CCFFFF",font=("FrankRuehl",20,"bold")).grid(column=0,row=0)
    d=Entry(f2,width=10)
    d.grid(column=1,row=0)
    en=Button(f3,text="Enter",justify=LEFT,bg="#CCFFFF",font=("FrankRuehl",20,"bold"),command=enter).pack()
    root2.mainloop()

def addbook():
    def enter():
        book=pd.read_csv("Book.csv")
        nm=id.get()
        if nm=="" or n=="" or a=="" or e=="":
            messagebox.showerror("Error","Invalid Syntax")
        else:
            tempbook=pd.DataFrame({"Book ID":id.get(),"Book Name":n.get(),"Author":a.get(),"Edition":e.get(),"Avalibility":"available"},index=[0])
            book=book.append(tempbook,ignore_index=True)
            book.to_csv("Book.csv",index=False)
            messagebox.showinfo("Sucessful","Added Sucessful")
            id.delete(0,len(id.get()))
            n.delete(0,len(n.get()))
            a.delete(0,len(a.get()))
            e.delete(0,len(e.get()))
    root2=Tk()
    root2.title("Add Book")
    root2.geometry("350x200")
    root2.resizable(0,0)
    f1=Frame(root2,background="#CCFFFF")
    f1.pack(expand=True,fill=BOTH)
    f2=Frame(root2,background="#CCFFFF")
    f2.pack(expand=True,fill=BOTH)
    f3=Frame(root2,background="#CCFFFF")
    f3.pack(expand=True,fill=BOTH)
    lable=Label(f1,text="Fill Book Details",justify=LEFT,bg="#CCFFFF",font=("FrankRuehl",20,"bold")).pack()
    idl=Label(f2,text="Book ID",justify=LEFT,bg="#CCFFFF",font=("FrankRuehl",20,"bold")).grid(column=0,row=0)
    id=Entry(f2,width=20)
    id.grid(column=1,row=0)
    nl=Label(f2,text="Book Name",justify=LEFT,bg="#CCFFFF",font=("FrankRuehl",20,"bold")).grid(column=0,row=1)
    n=Entry(f2,width=20)
    n.grid(column=1,row=1)
    al=Label(f2,text="Author",justify=LEFT,bg="#CCFFFF",font=("FrankRuehl",20,"bold")).grid(column=0,row=2)
    a=Entry(f2,width=20)
    a.grid(column=1,row=2)
    el=Label(f2,text="Edition",justify=LEFT,bg="#CCFFFF",font=("FrankRuehl",20,"bold")).grid(column=0,row=3)
    e=Entry(f2,width=20)
    e.grid(column=1,row=3)
    en=Button(f3,text="Enter",justify=LEFT,bg="#CCFFFF",font=("FrankRuehl",20,"bold"),command=enter).pack()
    root2.mainloop()

def listbooks():
    book=pd.read_csv("Book.csv")
    root2=Tk()
    root2.title("List of Books")
    lal=Label(root2,text=book,justify=LEFT,bg="#CCFFFF",font=("FrankRuehl",15)).pack(expand=True,fill=BOTH)
    root2.mainloop()

from tkinter import *

from doc import docito
from pat import pato

import cx_Oracle
def hosp():
    co='hospitaldb/dbms@localhost:1521/xe'
    conn=cx_Oracle.connect(co)
    cur=conn.cursor()


    root=Tk()
    root.title("Database Store")
    root.config(bg="#AC99F2") 
    root.geometry("500x500")
    root.iconbitmap("hos.ico")
    bg = PhotoImage(file = "C:/Users/admin/Downloads/dbms pic.png")
    label1 = Label( root, image = bg)
    label1.place(x=0,y=0)
    frame1 = Frame(root)
    frame1.pack(pady = 20 )

    def ok():
        docito()
    def ok1():
        pato()


    mylabel=Label(root,text="Hospital Details",font="times 20 bold",bg="#AC99F2")
    mylabel.pack()
    mylabel=Label(root,text="DBMS ABA",font="times 10 bold",bg="#AC99F2")
    mylabel.pack(side=BOTTOM)
    sqlc1='select * from hospital'
    cur.execute(sqlc1)
    r=cur.fetchall()
    print(r)

    for i in r:
        li=[]
        li.append(i)
        print(li)
        j=1
        i=0
        for j in li:
            label1=Label(root, text=j,relief=GROOVE,font=("Times",13,"bold"), bg='#ADD8E6')
            label1.pack(side=TOP)
            break

        
    b1=Button(root,text="Doctor", bg="grey",fg = "blue",width=9,height=1,font="times 20 bold",command=ok)
    b1.pack(pady='30')
    b2=Button(root,text="Patient", bg="grey",fg = "blue",width=9,height=1,font="times 20 bold",command=ok1)
    b2.pack()

    cur.close()
    conn.close()

    root.mainloop()
hosp()

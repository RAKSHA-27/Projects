from tkinter import *
from tkinter import messagebox
from sio import signo
import cx_Oracle

co='hospitaldb/dbms@localhost:1521/xe'
conn=cx_Oracle.connect(co)
cur=conn.cursor()

def pato():
    def ok():
        signo()
    def showp():

        sqlc1=("select * from pado where pid="+e1.get())
        sqlc2=("select pid from patient where pid="+e1.get())
        cur.execute(sqlc1)
        r=cur.fetchall()
        cur.execute(sqlc2)
        r1=cur.fetchall()
        print(r)
        lo=[]
        if r==lo:
                mylabel=Label(root1,text="Data not found : (",font="times 10 bold",bg="#AC99F2",fg="red")
                mylabel.pack()
                if r1!=lo:
                  mylabel=Label(root1,text="Data not UPDATED in DB by hospital : (",font="times 10 bold",bg="#AC99F2",fg="red")
                  mylabel.pack()
        else:
            for i in r:
                mylabel=Label(root1,text=i,font="times 10 bold",bg="#AC99F2")
                mylabel.pack()





    root1=Tk()
    root1.title("Database Store")
    root1.config(bg="#AC99F2") 
    root1.geometry("500x500")
    root1.iconbitmap("hos.ico")
    
    
  
    mylabel=Label(root1,text="Register if new...",font="times 17 bold",bg="#AC99F7")
    mylabel.pack()
    b3=Button(root1,text="Sign In",width=9,height=1,font="times 20 bold",command=ok)
    b3.pack(pady=20,padx=200)
    

    l1=Label(root1,text="Patient ID",font="times 10 bold",bg="#AC99F2")
    l1.pack(pady=1,padx=10)
    e1=Entry(root1)
    e1.pack(pady=10,padx=100)
    b4=Button(root1,text="Login",width=9,height=1,font="times 20 bold",command=showp)
    b4.pack()

    root1.mainloop()

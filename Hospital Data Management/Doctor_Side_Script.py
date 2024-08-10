
from tkinter import *
from tkinter import messagebox

import cx_Oracle
co='hospitaldb/dbms@localhost:1521/xe'
conn=cx_Oracle.connect(co)
cur=conn.cursor()
def docito():

    root3=Tk()
    root3.title("Database Store")
    root3.config(bg="#AC99F2") 
    root3.geometry("500x500")
    root3.iconbitmap("hos.ico")
    
    
    
    def outs(p):
        sqlc2=("select did from doctor where did="+e8.get())
        cur.execute(sqlc2)
        r1=cur.fetchall()
        print(r1)
        lo=[]
        if r1!=lo:
            sqlc1=("select * from pado where pid="+e7.get())
            cur.execute(sqlc1)
            r=cur.fetchall()
            print(r)
            if r==lo:
                mylabel=Label(root3,text="Results not found : (",font="times 10 bold",bg="#AC99F2",fg="red")
                mylabel.pack()
                mylabel=Label(root3,text="Check Patient ID / Patient data not UPDATED",font="times 10 bold",bg="#AC99F2",fg="red")
                mylabel.pack()
            else:
                for i in r:
                    mylabel=Label(root3,text=i,font="times 10 bold",bg="#AC99F2")
                    mylabel.pack()

        else:
             mylabel=Label(root3,text="Check the Doctor ID",font="times 10 bold",bg="#AC99F2",fg="red")
             mylabel.pack()
    #Save data to database table
    
    mylabel=Label(root3,text="Doctor Database",font="times 20 bold",bg="#AC99F2")
    mylabel.pack()
    l7=Label(root3,text="Patient ID",font="times 10 bold",bg="#AC99F2")
    l7.pack()
    global e7
    e7=Entry(root3)
    e7.pack()
    
    l8=Label(root3,text="Doctor ID",font="times 10 bold",bg="#AC99F2")
    l8.pack()
    e8=Entry(root3)
    e8.pack()
    b5=Button(root3,text="Show patient data",width=15,height=1,font="times 15 bold",command=lambda:outs(e7.get()))
    b5.pack(pady=10)
       
    root3.mainloop()
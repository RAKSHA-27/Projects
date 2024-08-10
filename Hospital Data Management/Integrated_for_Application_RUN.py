from tkinter import *
from tkinter import messagebox
import cx_Oracle
co='hospitaldb/dbms@localhost:1521/xe'
conn=cx_Oracle.connect(co)
cur=conn.cursor()
root=Tk()
root.title("Database Store")
root.geometry("700x700")

def ok():
    print("Works")
def showp():
   
    sqlc1='select * from patient'

    cur.execute(sqlc1)
    r=cur.fetchall()
    print(r)




def pat():
    root1=Tk()
    root1.title("Database Store")
    root1.geometry("500x500")
#Save data to database table
    mylabel=Label(root1,text="Register if new...",font="times 10 bold")
    mylabel.pack()
    b3=Button(root1,text="Sign In",width=9,height=1,font="times 20 bold",command=ok)
    b3.pack()
    l2=Label(root1,text="Patient ID",font="times 10 bold")
    l2.pack()
    e3=Entry(root1)
    e3.pack()
    l3=Label(root1,text="Patient Name",font="times 10 bold")
    l3.pack()
    e4=Entry(root1)
    e4.pack()
    l4=Label(root1,text="Hospital ID",font="times 10 bold")
    l4.pack()
    e5=Entry(root1)
    e5.pack()
    l5=Label(root1,text="Doctor ID",font="times 10 bold")
    l5.pack()
    e6=Entry(root1)
    e6.pack()

#Login shows patient details table -- Done
    b4=Button(root1,text="Login",width=9,height=1,font="times 20 bold",command=showp)
    b4.pack()
    l1=Label(root1,text="Patient ID",font="times 10 bold")
    l1.pack()
    e1=Entry(root1)
    e1.pack()

    root1.mainloop()
def doc():
    root2=Tk()
    root2.title("Database Store")
    root2.geometry("500x500")
    def outs(p):
        print(p)
        sqlc1=("select * from pado where pid="+a)
        cur.execute(sqlc1)
        r=cur.fetchall()
        print(r)
        for i in r:
            mylabel=Label(root,text=i,font="times 10 bold")
            mylabel.pack()
        for i in range(0,2):
            mylabel=Label(root2,text=r[i],font="times 10 bold")
            mylabel.pack()
#Save data to database table
    mylabel=Label(root2,text="Doctor Database",font="times 20 bold")
    mylabel.pack()
    l7=Label(root2,text="Patient ID",font="times 10 bold")
    l7.pack()
    global e7
    e7=Entry(root2)
    e7.pack()
    l8=Label(root2,text="Doctor ID",font="times 10 bold")
    l8.pack()
    e8=Entry(root2)
    e8.pack()
    b5=Button(root2,text="Show patient data",width=15,height=1,font="times 15 bold",command=lambda:outs(e7.get()))
    b5.pack()
    root2.mainloop()
    #Show the patient data table
#Hospital table to be displayed code

mylabel=Label(root,text="Hospital Details",font="times 20 bold")
mylabel.pack()
sqlc1='select * from hospital'
cur.execute(sqlc1)
r=cur.fetchall()
print(r)
for i in range(0,3):
    mylabel=Label(root,text=r[i],font="times 10 bold")
    mylabel.pack()
b1=Button(root,text="Doctor",width=9,height=1,font="times 20 bold",command=doc)
b1.pack()
b2=Button(root,text="Patient",width=9,height=1,font="times 20 bold",command=pat)
b2.pack()

cur.close()
conn.close()

root.mainloop()

from tkinter import *
from tkinter.ttk import *
import tkinter as tk


window = Tk()
window.geometry("450x900")
window['bg']='purple'

#put your name and birth date
def open_popup():
   top= Toplevel(window)
   top['bg'] = 'purple'
   top.geometry("450x300")
   top.title("กรอกชื่อ-นามสกุล")
   user_name = Label(top,text = "ขื่อ").place(x = 20,y = 20) 
   name = Text(top, width=40, height=2)
   name.place(x=120,y=10)
   name2 = Text(top, width=40, height=2)
   name2.place(x=120,y=75)
   user_name2 = Label(top,text = "นามสกุล").place(x = 20,y = 75)
   bd = Text(top, width=40, height=2)
   bd.place(x=120,y=155)
   bd1 = Label(top,text = "วันเกิด").place(x = 20,y = 155)  
   bar3 = Button(top,text='ไปทำนายดวง',command=occl)
   bar3.place(x=295,y=255)

#the card chart choose cards 
def occl():
   oc= Toplevel(window)
   oc['bg'] = 'purple'
   oc.geometry("650x1200")
   oc.title("Occlumency")
   tarot = Button(oc,image=photo2,command=focl1)
   tarot.place(x=45,y=50)

   tarot = Button(oc,image=photo2)
   tarot.place(x=225,y=50)

   tarot = Button(oc,image=photo2)
   tarot.place(x=425,y=50)

   tarot = Button(oc,image=photo2)
   tarot.place(x=45,y=300)

   tarot = Button(oc,image=photo2)
   tarot.place(x=225,y=300)

   tarot = Button(oc,image=photo2)
   tarot.place(x=425,y=300)

   tarot = Button(oc,image=photo2)
   tarot.place(x=45,y=550)

   tarot = Button(oc,image=photo2)
   tarot.place(x=225,y=550)

   tarot = Button(oc,image=photo2)
   tarot.place(x=425,y=550)
   
# The divination results // they will be more in the future
def focl1():
   focl= Toplevel(window)
   focl['bg'] = 'purple'
   focl.geometry("650x1200")
   focl.title("The High Priest")
   
   priest = Button(focl,image=photo4)
   priest.place(x=95,y=300)
   
   
#locate where you dowload the pictures
photo1 = PhotoImage(file="C:/Users/finpu/Desktop/PHC5project/logo.png")
bar2 = Button(window,image=photo1,command=open_popup)
bar2.place(x=95,y=300)
photo2 = PhotoImage(file="C:/Users/finpu/Desktop/PHC5project/tarot.png")
photo4 = PhotoImage(file="C:/Users/finpu/Desktop/PHC5project/priest.png")



window.mainloop()

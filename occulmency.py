from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from matplotlib.font_manager import weight_dict

window = Tk()
window.geometry("450x700")
window.title('Occlumency')

background_image=tk.PhotoImage(file="C:/Users/finpu/Desktop/PHC5project/bg.png")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

window.resizable(False, False)

def open_popup():
   top= Toplevel(window)
   top.geometry("600x350")
   top.title("กรอกชื่อ-นามสกุล")

   background_image3=tk.PhotoImage(file="C:/Users/finpu/Desktop/PHC5project/bg2.png")
   background_label3 = tk.Label(top, image=background_image)
   background_label3.place(x=0, y=0, relwidth=1, relheight=1)

   # name
   user_name = Label(top,text = "ชื่อ", font=('Times New Roman', 20)).place(x = 25,y = 50) 
   name = Text(top, width=25, height=0.5, font=('Times New Roman', 20))
   name.place(x=220,y=50)

   # surname
   user_name2 = Label(top,text = "นามสกุล", font=('Times New Roman', 20)).place(x = 20,y = 135)
   name2 = Text(top, width=25, height=0.5, font=('Times New Roman', 20))
   name2.place(x=220,y=135)
  
   #birth
   bd1 = Label(top,text = "วันเกิด", font=('Times New Roman', 20)).place(x = 20,y = 215)
   bd = Text(top, width=25, height=0.5, font=('Times New Roman', 20))
   bd.place(x=220,y=215)
     
   #button
   bar3 = Button(top,text='ไปทำนายกันเลยย',command=occl)
   bar3.place(x=500,y=305)


def occl():
   oc= Toplevel(window)
   oc['bg'] = 'purple'
   oc.geometry("650x1200")
   oc.title("Occlumency")

   background_image1=tk.PhotoImage(file="C:/Users/finpu/Desktop/PHC5project/bg2.png")
   background_label1 = tk.Label(oc, image=background_image)
   background_label1.place(x=0, y=0, relwidth=1, relheight=1)


   # row 1
   tarot = Button(oc,image=photo2,command=focl1)
   tarot.place(x=75,y=50)

   tarot = Button(oc,image=photo2)
   tarot.place(x=275,y=50)

   tarot = Button(oc,image=photo2)
   tarot.place(x=475,y=50)

   #row2
   tarot = Button(oc,image=photo2)
   tarot.place(x=75,y=300)

   tarot = Button(oc,image=photo2)
   tarot.place(x=275,y=300)

   tarot = Button(oc,image=photo2)
   tarot.place(x=475,y=300)

   #row3
   tarot = Button(oc,image=photo2)
   tarot.place(x=75,y=570)

   tarot = Button(oc,image=photo2)
   tarot.place(x=275,y=570)

   tarot = Button(oc,image=photo2)
   tarot.place(x=475,y=570)

def focl1():
   focl= Toplevel(window)
   focl['bg'] = 'purple'
   focl.geometry("350x650")
   focl.title("The High Priest")

   background_image2=tk.PhotoImage(file="C:/Users/finpu/Desktop/PHC5project/bg2.png")
   background_label2 = tk.Label(focl, image=background_image)
   background_label2.place(x=0, y=0, relwidth=1, relheight=1)
   
   priest = Button(focl,image=photo4)
   priest.place(x=85,y=75)

   dive = Button(focl,image=photo5)
   dive.place(x=115,y=475)
   
   
# txt = Label(window, text="Comparerameter", font=("Arial Bold", 10))
# txt.grid(column=0, row=1)




#imageeee
photo1 = PhotoImage(file="C:/Users/finpu/Desktop/PHC5project/lg.png")
photo2 = PhotoImage(file="C:/Users/finpu/Desktop/PHC5project/tarot.png")
photo4 = PhotoImage(file="C:/Users/finpu/Desktop/PHC5project/th.png")
photo5 = PhotoImage(file="C:/Users/finpu/Desktop/PHC5project/dv.png")


bar2 = Button(window,image=photo1,command=open_popup)
bar2.place(x=95,y=205)


window.mainloop()

# import tkinter
#
# m=tkinter.Tk(className='First window')
# m.mainloop()

# Widgets

#   Button
# import tkinter as tk
#
# r=tk.Tk()
# r.title('Counting seconds')
# button=tk.Button(r, text='Yello',width=25,highlightbackground='#ccff00')
# button.grid(row=0)
# button1=tk.Button(r, text='Stop',width=25,highlightbackground='red')
# button1.grid(row=1,column=1)
# r.mainloop()

#   Canvas

# from tkinter import *
#
# master=Tk()
# w=Canvas(master,width=200,height=100,bg='blue')
# w.pack()
# w.create_line(0,10,200,10)
# mainloop()

#   Checkpoint

# from tkinter import *
#
# master=Tk()
# var1=IntVar()
# Checkbutton(master,text='male',variable=var1).grid(row=0,sticky='W')
# var2=IntVar()
# Checkbutton(master,text='female',variable=var2).grid(row=1,sticky='W')
# mainloop()

#   Label
# from tkinter import *
#
# master=Tk()
# w=Label(master,text='My first label')
# w.pack()
# master.mainloop()

#   Entry
# from tkinter import *
#
# master =Tk()
# Label(master,text='First name').grid(row=0)
# Label(master,text='Second name').grid(row=1)
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)
# mainloop()



#   Frame

# from tkinter import *
#
# root=Tk()
# frame=Frame(root)
# frame.pack()
# bottomframe=Frame(root)
# bottomframe.pack(side = BOTTOM)
# redbutton=Button(frame,text='Red',highlightbackground='red',fg='red')
# redbutton.pack(side = RIGHT)
# greenbutton=Button(frame,text='Green',highlightbackground='green',fg='green')
# greenbutton.pack(side = LEFT)
# bluebutton=Button(frame,text='Blue',highlightbackground='blue',fg='blue')
# bluebutton.pack(side = LEFT)
# blackbutton=Button(bottomframe,text='Black',highlightbackground='black',fg='black')
# blackbutton.pack(side = BOTTOM)
# root.mainloop()

#   ListBox

# from tkinter import *
#
# top = Tk()
# Lb = Listbox(top)
# Lb.insert(1,'Python')
# Lb.insert(2,'Java')
# Lb.insert(3,'C++')
# Lb.insert(4,'Any')
# Lb.pack()
# mainloop()


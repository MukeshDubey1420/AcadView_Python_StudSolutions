#MenuButton
# from tkinter import *
#
# top = Tk()
# mb = Menubutton(top, text= "Menu")
# mb.grid()
# mb.menu = Menu(mb)
# mb['menu']= mb.menu
# cVar = IntVar()
# aVar = IntVar()
# mb.menu.add_checkbutton(label='Contact', variable=cVar)
# mb.menu.add_checkbutton(label='About', variable=aVar)
# print(cVar.get(),aVar.get())
# mb.pack()
# top.mainloop()

#Menu
# from tkinter import *
#
# root = Tk()
# menu = Menu(root)
# root.config(menu=menu)
# filemenu = Menu(menu)
# menu.add_cascade(label='File', menu=filemenu)
# filemenu.add_command(label='New')
# filemenu.add_command(label='Open...')
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=root.quit)
# helpmenu = Menu(menu)
# menu.add_cascade(label='Help', menu=helpmenu)
# helpmenu.add_command(label='About')
# mainloop()

#Message
# from tkinter import *
# main = Tk()
# ourMessage ='Am I a label? No clue'
# messageVar = Message(main, text = ourMessage)
# messageVar.config(bg='lightgreen')
# messageVar.pack( )
# mainloop( )

#Radio Button
# from tkinter import *
# root = Tk()
# v = IntVar()
# Radiobutton(root, text='Yello', variable=v, value=1).pack(anchor=W)
# Radiobutton(root, text='Jello', variable=v, value=2).pack(anchor=W)
# mainloop()

#Scale
# from tkinter import *
# master = Tk()
# w = Scale(master, from_=0, to=42)
# w.pack()
# w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
# w.pack()
# mainloop()

#Scrollbar
# from tkinter import *
# root = Tk()
# scrollbar = Scrollbar(root)
# scrollbar.pack( side = RIGHT, fill = Y )
# mylist = Listbox(root, yscrollcommand = scrollbar.set )
# for line in range(100):
#    mylist.insert(END, 'This is line number' + str(line))
# mylist.pack( side = LEFT, fill = BOTH )
# scrollbar.config( command = mylist.yview )
# mainloop()

#Text
# from tkinter import *
# root = Tk()
# T = Text(root, height=20, width=30)
# T.pack()
# T.insert(END, 'Yello\nJello\n')
# mainloop()

#TopLevel
# from tkinter import *
# root = Tk()
# root.title('First')
# top = Toplevel()
# top.title('Second')
# T = Text(top, height=20, width=30)
# T.pack()
# T.insert(END, 'Yello\nJello\n')
# top.mainloop()

#SpinBox
# from tkinter import *
# master = Tk()
# w = Spinbox(master, from_ = 0, to = 10)
# w.pack()
# mainloop()

#Paned Window
# from tkinter import *
# m1 = PanedWindow()
# m1.pack(fill = BOTH, expand = 1)
# left = Entry(m1, bd = 5)
# m1.add(left)
# m2 = PanedWindow(m1, orient = VERTICAL)
# m1.add(m2)
# top = Scale( m2, orient = HORIZONTAL)
# m2.add(top)
# mainloop()

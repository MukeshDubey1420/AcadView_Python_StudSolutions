# from tkinter import *
# import vlc
#
#
# def clickme():
#     print('Clicked!')
#     l=Label(mainscreen,text='Clicked')
#     l.pack(side=BOTTOM)
# def playme():
#     p = vlc.MediaPlayer("Twin-Peaks-Packards.mp3")
#     p.play()
#     while True: pass
# def checkme(var):
#     l = Label(mainscreen, text=var)
#     l.pack(side=BOTTOM)
#
#
# mainscreen=Tk()
# playButton=Button(mainscreen,text='Play',highlightbackground='#ccff00',command=clickme)
# playButton.grid(row=0)
# playMeButton=Button(mainscreen,text='Music',highlightbackground='#ff346d',command=playme)
# playMeButton.grid(row=0,column=1)
#
# var1=IntVar()
# print(var1.get())
# Checkbutton(mainscreen,text='male',variable=var1,command=lambda :checkme(var1.get())).grid(row=1,sticky='W')
# var2=IntVar()
# Checkbutton(mainscreen,text='female',variable=var2,command=lambda :checkme(var2.get())).grid(row=2,sticky='W')
# close=Button(mainscreen,text='Close',command=sys.exit)
# close.grid(row=4, column=1)
# mainloop()
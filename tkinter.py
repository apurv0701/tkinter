from sys import exit as e
from tkinter import *
root = Tk()
def main ():
    #root = Tk()
    button = Button(master=root,activebackground = "blue",
                    text='hello',
                    command = quit_callback)
    button.pack()
    
    #root = Tk()
    button = Button(root,text='h',command = quit_callback)
    button.pack()
    root.mainloop()
   
def quit_callback():
    #sys.exit(0)
    e(0)
    
#no change, only to see difference on GitHub

    #add design
def design():
   # root = Tk()
    w = Canvas(root, width=40, height=60)
    w.grid()
    canvas_height=20
    canvas_width=200
    y = int(canvas_height / 2)
    w.create_line(0, y, canvas_width, y )

    #add checkbox
def checkbox():
    #root = Tk()
    root.title('choose gender')

    var1 = IntVar()
    Checkbutton(root, text='male', variable=var1).grid(row=0, sticky=W)
    var2 = IntVar()
    Checkbutton(root, text='female', variable=var2).grid(row=1, sticky=W)
   # Checkbutton.pack()
   
    #add label
def label() :
    #root = Tk()
    Label(root, text='First Name').grid(row=0)
    Label(root, text='Last Name').grid(row=1)
    e1 = Entry(root)
    e2 = Entry(root)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)


    #frame
def frame():
    frame = Frame(root)
    frame.pack()
    bottomframe = Frame(root)
    bottomframe.pack( side = TOP )
    redbutton = Button(frame, text = 'Red', fg ='red')
    redbutton.pack( side = RIGHT)
    greenbutton = Button(frame, text = 'Brown', fg='brown')
    greenbutton.pack( side = LEFT )
    bluebutton = Button(frame, text ='Blue', fg ='blue')
    bluebutton.pack( side = LEFT )
    blackbutton = Button(bottomframe, text ='Black', fg ='black')
    blackbutton.pack( side = BOTTOM)
    #root.mainloop()    

    #LABEL
def label():
    w = Label(root, text='GeeksForGeeks.org!')
    w.pack()
    root.mainloop()

    #listbox
def listbox():
   
    Lb = Listbox(root)
    Lb.insert(1, 'Python')
    Lb.insert(2, 'Java')
    Lb.insert(3, 'C++')
    Lb.insert(4, 'Any other')
    Lb.pack()
    root.mainloop()
   


#main()
#design()
#checkbox()
#label()
#frame()
#label()
listbox()





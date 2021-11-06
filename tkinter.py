#fill argument in pack method− Determines whether widget fills any extra space allocated to it by the packer,

#or keeps its own minimal dimensions: NONE (default), X (fill only horizontally),

#Y (fill only vertically), or BOTH (fill both horizontally and vertically).

 

 

   

from tkinter import *

 

num1=0

num2=0

 

root = Tk()

 

 

def pressed_button_1():

    global num1

    num1=1

    print("one")

 

def pressed_button_2():

    global num1

    num1=2

    print("two")

 

def pressed_button_3():

    global num1

    num1=3

    print("three") 

    

def pressed_button_4():

    global num1

    num1 =4

    print("four")

 

def pressed_button_5():

    global num1

    num1=5

    print("five")

 

def pressed_button_6():

    global num1

    num1=6

    print("six")

 

def pressed_button_7():

    global num1

    num1=7

    print("seven")

 

def pressed_button_8():

    global num1

    num1=8

    print("eight")

 

def pressed_button_9():

    global num1

    num1=9

    print("nine")

 

def pressed_button_0():

    global num1

    num1=0

    print("zero")

   

 

def pressed_button_add():

    ans = num1 + num2

    print("add")

    print(ans)

   

 

def pressed_button_sub():

    ans = num1 - num2

    print("subtraction")

    print(ans)

 

def pressed_button_mul():

    ans = num1 * num2

    print("mutiplication")

    print(ans)

 

def pressed_button_div():

    ans = num1 / num2

    print("division")

    print(ans)

 

def main():

   root.title("STANDARD CALCULATOR")

   root.geometry('300x300')

 

   frame = Frame(root)

   frame.pack()

 

  # equation2 = IntVar()

   #expression_field2 = Entry(root, textvariable=equation2)

   #expression_field2.grid(columnspan=4, ipadx=70)

 

   #equation2.set('Value in Hex')

 

   button_1 = Button(frame , text = '1', command=pressed_button_1)

   button_1.grid(column = 1 ,row =1)

 

 

  button_2 = Button(frame , text = '4',command=pressed_button_4 )

   button_2.grid(column = 1 ,row = 2)

  

   button_3 = Button(frame , text = '7',command=pressed_button_7 )

   button_3.grid(column = 1 ,row =3)

  

   button_4 = Button(frame , text = '2',command=pressed_button_2 )

   button_4.grid(column = 2,row =1 )

  

   button_5 = Button(frame , text = '5',command=pressed_button_5 )

   button_5.grid(column = 2,row =2 )

  

   button_6 = Button(frame , text = '8',command=pressed_button_8 )

   button_6.grid(column = 2,row =3 )

  

   button_7 = Button(frame , text = '3',command=pressed_button_3 )

   button_7.grid(column = 3,row=1 )

  

   button_8 = Button(frame , text = '6',command=pressed_button_6 )

   button_8.grid(column = 3 ,row=2)

  

   button_9 = Button(frame , text = '9',command=pressed_button_9 )

   button_9.grid(column = 3,row =3  )

  

   button_0 = Button(frame , text = '0',command=pressed_button_0)

   button_0.grid(column = 2 )

 

   button_add = Button(frame , text = '+' ,command=pressed_button_add )

   button_add.grid(column=1,row=4 )

 

   button_sub = Button(frame , text = '-',command=pressed_button_sub )

   button_sub.grid(column = 3, row = 4 )

 

   button_mul = Button(frame , text = '*',command=pressed_button_mul )

   button_mul.grid(column = 4, row =4  )

  

   button_div = Button(frame , text = '/',command=pressed_button_div )

   button_div.grid(column = 3, row =5  )

   root.mainloop()

  

main()
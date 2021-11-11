#fill argument in pack method− Determines whether widget fills any extra space allocated to it by the packer,

#or keeps its own minimal dimensions: NONE (default), X (fill only horizontally),

#Y (fill only vertically), or BOTH (fill both horizontally and vertically).

#-------------------------------------------------------------------

# lambda function :the lambda keyword is used to define an anonymous function in Python. 

#-------------------------------------------------------------------

# parameter of Button

 # w = Button ( master, option=value, ... )

 
   

from tkinter import *



root = Tk() #used for creating a parent window
expression = ""
equation = StringVar()
expression_field = Entry(root, textvariable=equation)
def press(num):
    # point out the global expression variable
    global expression
 
    # concatenation of string
    expression = expression + str(num)
 
    # update the expression by using set method
    equation.set(expression)
    
    
def temp():
    print("HELLO WORLD !")
    
 


def main():

   root.title("STANDARD CALCULATOR")#title used for naming parent window

   root.geometry('300x300')#geometry used for specifying the size of parent window
   root.configure(background = 'yellow')
 

   frame = Frame(root)

   frame.pack()
   
   equation = StringVar()
   expression_field = Entry(root, textvariable=equation)
 
   button_1 = Button(frame , text = '1' ,command=lambda: press(1)
                      )
   button_1.grid(column = 1 ,row =1)

 
   button_2 = Button(frame , text = '4' )

   button_2.grid(column = 1 ,row = 2)

  

   button_3 = Button(frame , text = '7' )

   button_3.grid(column = 1 ,row =3)

  

   button_4 = Button(frame , text = '2' )

   button_4.grid(column = 2,row =1 )

  

   button_5 = Button(frame , text = '5' )

   button_5.grid(column = 2,row =2 )

  

   button_6 = Button(frame , text = '8' )

   button_6.grid(column = 2,row =3 )

  

   button_7 = Button(frame , text = '3' )

   button_7.grid(column = 3,row=1 )

  

   button_8 = Button(frame , text = '6' )

   button_8.grid(column = 3 ,row=2)

  

   button_9 = Button(frame , text = '9' )

   button_9.grid(column = 3,row =3  )

  

   button_0 = Button(frame , text = '0')

   button_0.grid(column = 2 )

 

   button_add = Button(frame , text = '+' )

   button_add.grid(column=1,row=4 )

 

   button_sub = Button(frame , text = '-' )

   button_sub.grid(column = 3, row = 4 )

 

   button_mul = Button(frame , text = '*' )

   button_mul.grid(column = 1 , row =5  )

  

   button_div = Button(frame , text = '/' )

   button_div.grid(column = 2, row =5  )

   button_mod = Button(frame , text= '%' )
   button_mod.grid(row=5 , column =3)

   test =Button(frame , text = "TEST",activebackground = 'blue',
                activeforeground = 'red' , bg = 'green' ,
                bd= 2 , command = temp,height =5 , width = 3)
   
   test.grid(row = 6 , column = 2) #default value of row and column is 0

   root.mainloop()#Use mainloop() to call the endless loop of the window

  

main()

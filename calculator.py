# Python program to create a simple calc

from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expression

def press(num):
	# point out the global expression variable
	global expression

	# concatenation of string
	expression = expression + str(num)

	# update the expression by using set method
	equation.set(expression)


# Function to evaluate the final expression
def equalpress():
	# Try and except statement is used
	# for handling the errors like zero
	# division error etc.

	# Put that code inside the try block
	# which may generate the error
	try:

		global expression

		# eval function evaluate the expression
		# and str function convert the result
		# into string
		total = str(eval(expression))

		equation.set(total)

		
		expression = ""

	
	except:

		equation.set(" error ")
		expression = ""



def delete():
	global expression
	expression = ""
	equation.set("")



calc = Tk()
calc.geometry('485x385')
calc.configure(background="lightgrey")
calc.title("Simple Calculator")

equation = StringVar()

expression_field = Entry(calc,font=(20),textvariable=equation,width=59)
expression_field.place(x=2,y=2,height=60)

clear = Button(calc, text='AC', fg='white', bg='blue',
command=delete, height=3, width=15)
clear.place(x=365, y=5)

button1 = Button(calc, text=' 1 ', fg='white', bg='blue',
command=lambda: press(1), height=4, width=15)
button1.place(x=5, y=70)

button2 = Button(calc, text=' 2 ', fg='white', bg='blue',
command=lambda: press(2), height=4, width=15)
button2.place(x=125, y=70)

button3 = Button(calc, text=' 3 ', fg='white', bg='blue',
command=lambda: press(3), height=4, width=15)
button3.place(x=245, y=70)

button4 = Button(calc, text=' 4 ', fg='white', bg='blue',
command=lambda: press(4), height=4, width=15)
button4.place(x=5, y=150)

button5 = Button(calc, text=' 5 ', fg='white', bg='blue',
command=lambda: press(5), height=4, width=15)
button5.place(x=125, y=150)

button6 = Button(calc, text=' 6 ', fg='white', bg='blue',
command=lambda: press(6), height=4, width=15)
button6.place(x=245, y=150)

button7 = Button(calc, text=' 7 ', fg='white', bg='blue',
command=lambda: press(15), height=4, width=15)
button7.place(x=5, y=230)

button8 = Button(calc, text=' 8 ', fg='white', bg='blue',
command=lambda: press(8), height=4, width=15)
button8.place(x=125, y=230)

button9 = Button(calc, text=' 9 ', fg='white', bg='blue',
command=lambda: press(9), height=4, width=15)
button9.place(x=245, y=230)

button0 = Button(calc, text=' 0 ', fg='white', bg='blue',
command=lambda: press(0), height=4, width=15)
button0.place(x=5, y=310)

plus = Button(calc, text=' + ', fg='white', bg='blue',
command=lambda: press("+"), height=4, width=15)
plus.place(x=365, y=70)

minus = Button(calc, text=' - ', fg='white', bg='blue',
command=lambda: press("-"), height=4, width=15)
minus.place(x=365, y=150)

multiply = Button(calc, text=' * ', fg='white', bg='blue',
command=lambda: press("*"), height=4, width=15)
multiply.place(x=365, y=230)

divide = Button(calc, text=' / ', fg='white', bg='blue',
command=lambda: press("/"), height=4, width=15)
divide.place(x=365, y=310)

Dec= Button(calc, text='.', fg='white', bg='blue',
command=lambda: press('.'), height=4, width=15)
Dec.place(x=125, y=310)

equal = Button(calc, text=' = ', fg='white', bg='blue',
command=equalpress, height=4, width=15)
equal.place(x=245, y=310)

# start the calc
calc.mainloop()

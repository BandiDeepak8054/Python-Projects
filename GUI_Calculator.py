import tkinter as tk
from tkinter.ttk import Button
from tkinter import Entry
expression  = ''
def press(number):
    global expression
    expression = expression + str(number)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ''
    equation.set('')
if __name__ =="__main__":
    gui = tk.Tk()
    gui.configure(background='light green')
    gui.title('Calculator')
    gui.geometry('290x150')
    equation = tk.StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

    button1 =Button(gui,text = '1',command=lambda:press(1))
    button1.grid(row=2,column=0)

    button2 = Button(gui, text=' 2 ',command=lambda: press(2))
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ',command=lambda: press(3))
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ',command=lambda: press(4))
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ',command=lambda: press(5))
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ',command=lambda: press(6))
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ',command=lambda: press(7))
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ',command=lambda: press(8))
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ',command=lambda: press(9))
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ',command=lambda: press(0))
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ',command=lambda: press("+"))
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ',command=lambda: press("-"))
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ',command=lambda: press("*"))
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ',command=lambda: press("/"))
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ',command=equalpress)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear',command=clear)
    clear.grid(row=5, column='1')

    Decimal= Button(gui, text='.',command=lambda: press('.'))
    Decimal.grid(row=6, column=0)
    gui.mainloop()
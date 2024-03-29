from tkinter import *

win = Tk()

win.title("Simple Calculator")

e = Entry(win, width=35, borderwidth=15, bg="cyan")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_mul():
    first_number = e.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math_operation == "addition":
        e.insert(0, f_num + int(second_number))
    elif math_operation == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math_operation == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math_operation == "division":
        e.insert(0, f_num / int(second_number))

button_1 = Button(win, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(win, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(win, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(win, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(win, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(win, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(win, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(win, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(win, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(win, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(win, text="+", padx=40, pady=20, command=button_add)
button_sub = Button(win, text="-", padx=40, pady=20, command=button_sub)
button_mul = Button(win, text="*", padx=40, pady=20, command=button_mul)
button_div = Button(win, text="/", padx=40, pady=20, command=button_div)
button_equal = Button(win, text="=", padx=40, pady=20, command=button_equal)
button_clear = Button(win, text="Clear", padx=79, pady=20, command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_equal.grid(row=5, column=0, columnspan=4)

win.mainloop()#   t r r  
 
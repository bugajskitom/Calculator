from tkinter import *

root = Tk()
root.title('Kalkulator')
root.configure(bg="black")

e = Entry(root,width=14,font=("Verdana", 18),bg="black", fg="white", border=0)
e.pack(pady=10,padx=16)

my_frame = Frame(root, bg="black")
my_frame.pack(padx=16, pady=14)

def button_click(number):
    e.insert(len(e.get()), str(number))

def button_operator(operator):
    if e.get()[-1] != "+" and e.get()[-1] != "-" and e.get()[-1] != "*" and e.get()[-1] != "/" and e.get()[-1] != ".":
        e.insert(len(e.get()), str(operator))

def button_delete():
    e.delete(len(e.get())-1)

def button_clear():
    e.delete(0, END)


def button_result():
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(round(eval(result), 8)))



button_plus = Button(my_frame, text="+", font=("Verdana", 24), width=2, padx=2, command=lambda: button_operator("+"), bg="black", fg="white")
button_plus.grid(row=0, column=3)

button_minus = Button(my_frame, text="-", font=("Verdana", 24), width=2, padx=2, command=lambda: button_operator("-"), bg="black", fg="white")
button_minus.grid(row=1, column=3)

button_mult = Button(my_frame, text="*", font=("Verdana", 24), width=2, padx=2, command=lambda: button_operator("*"), bg="black", fg="white")
button_mult.grid(row=2, column=3)

button_div = Button(my_frame, text="/", font=("Verdana", 24), width=2, padx=2, command=lambda: button_operator("/"), bg="black", fg="white")
button_div.grid(row=3, column=3)

button_dot = Button(my_frame, text=".", font=("Verdana", 24), width=2, padx=2, command=lambda: button_operator("."), bg="black", fg="white")
button_dot.grid(row=4, column=0)

button_delete = Button(my_frame, text="<-", font=("Verdana", 24), width=2, padx=2, command=button_delete, bg="black", fg="white")
button_delete.grid(row=0, column=2)

button_clear = Button(my_frame, text="Clear", font=("Verdana", 22), width=5, padx=2, pady=4, bg="black", fg="white", command=button_clear)
button_clear.grid(row=0, column=0, columnspan=2)

button0 = Button(my_frame, text="0", font=("Verdana", 24), width=2, padx=2, command=lambda: button_click(0), bg="black", fg="white")
button0.grid(row=4, column=1)

button1 = Button(my_frame, text="1", font=("Verdana", 24), width=2, padx=2, command=lambda: button_click(1), bg="black", fg="white")
button1.grid(row=3, column=0)

button2 = Button(my_frame, text="2", font=("Verdana", 24), width=2, padx=2, command=lambda: button_click(2), bg="black", fg="white")
button2.grid(row=3, column=1)

button3 = Button(my_frame, text="3", font=("Verdana", 24), width=2, padx=2, command=lambda: button_click(3), bg="black", fg="white")
button3.grid(row=3, column=2)

button4 = Button(my_frame, text="4", font=("Verdana", 24), width=2, padx=2, command=lambda: button_click(4), bg="black", fg="white")
button4.grid(row=2, column=0)

button5 = Button(my_frame, text="5", font=("Verdana", 24), width=2, padx=2, command=lambda: button_click(5), bg="black", fg="white")
button5.grid(row=2, column=1)

button6 = Button(my_frame, text="6", font=("Verdana", 24), width=2, padx=2, command=lambda: button_click(6), bg="black", fg="white")
button6.grid(row=2, column=2)

button7 = Button(my_frame, text="7", font=("Verdana", 24), width=2, padx=2, command=lambda: button_click(7), bg="black", fg="white")
button7.grid(row=1, column=0)

button8 = Button(my_frame, text="8", font=("Verdana", 24), width=2, padx=2, command=lambda: button_click(8), bg="black", fg="white")
button8.grid(row=1, column=1)

button9 = Button(my_frame, text="9", font=("Verdana", 24), width=2, padx=2, command=lambda: button_click(9), bg="black", fg="white")
button9.grid(row=1, column=2)

button_result = Button(my_frame, text="=", font=("Verdana", 22), width=5, padx=2, pady=4, bg="#220066", fg="white", command=button_result)
button_result.grid(row=4, column=2, columnspan=2)


root.mainloop()


import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


window = tk.Tk()
window.title('Calculator')


# size of the window
window.geometry("350x350")
window.resizable(False, False)

# add and place +, -, /, * buttons
button_add = tk.Button(window, text='+', command=add)
button_add.place(x=100, y=200, width=20, height=30)
button_sub = tk.Button(window, text='-', command=sub)
button_sub.place(x=150, y=200, width=20, height=30)
button_mul = tk.Button(window, text='*', command=mul)
button_mul.place(x=200, y=200, width=20, height=30)
button_div = tk.Button(window, text='/', command=div)
button_div.place(x=250, y=200, width=20, height=30)

# add and place entry for numbers
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=70, y=100)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=70, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=70, y=280)

# add and place text information for user
number1 = tk.Label(window, text='Enter first number:')
number1.place(x=70, y=80)
number2 = tk.Label(window, text='Enter second number:')
number2.place(x=70, y=130)
answer = tk.Label(window, text='Answer:')
answer.place(x=70, y=250)

window.mainloop()


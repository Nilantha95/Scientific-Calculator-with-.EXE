import tkinter as tk
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x650+550+100")
root.resizable(False, False)
root.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            equation_mod = equation.replace('^', '**')
            equation_mod = equation_mod.replace('sin', 'math.sin')
            equation_mod = equation_mod.replace('cos', 'math.cos')
            equation_mod = equation_mod.replace('tan', 'math.tan')
            equation_mod = equation_mod.replace('log', 'math.log')
            equation_mod = equation_mod.replace('sqrt', 'math.sqrt')
            result = eval(equation_mod)
        except Exception as e:
            result = "error"
            equation = ""
        label_result.config(text=result)

def key_press(event):
    key = event.char
    if key.isdigit() or key in ".+-*/()^":
        show(key)
    elif key in ["\r", "\n"]:
        calculate()
    elif key == "c":
        clear()
    elif event.keysym == "Escape":
        clear()

def handle_backspace(event):
    global equation
    equation = equation[:-1]
    label_result.config(text=equation)

frame = tk.Frame(root, bd=2, relief="solid")
frame.pack(pady=10)

label_result = tk.Label(root, width=23, height=0, text="", font=("arial", 20))
label_result.pack(pady=(0, 50))
label_result.pack()

button_font = ("arial", 20, "bold")

tk.Button(root, text="C", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#3697f5", command=lambda: clear()).place(x=10, y=80)
tk.Button(root, text="/", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/")).place(x=110, y=80)
tk.Button(root, text="%", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("%")).place(x=210, y=80)
tk.Button(root, text="*", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*")).place(x=310, y=80)

tk.Button(root, text="7", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#3697f5", command=lambda: show("7")).place(x=10, y=160)
tk.Button(root, text="8", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8")).place(x=110, y=160)
tk.Button(root, text="9", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9")).place(x=210, y=160)
tk.Button(root, text="-", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-")).place(x=310, y=160)

tk.Button(root, text="4", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#3697f5", command=lambda: show("4")).place(x=10, y=240)
tk.Button(root, text="5", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5")).place(x=110, y=240)
tk.Button(root, text="6", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6")).place(x=210, y=240)
tk.Button(root, text="+", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+")).place(x=310, y=240)

tk.Button(root, text="1", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#3697f5", command=lambda: show("1")).place(x=10, y=320)
tk.Button(root, text="2", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2")).place(x=110, y=320)
tk.Button(root, text="3", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).place(x=210, y=320)
tk.Button(root, text="0", width=10, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).place(x=10, y=400)

tk.Button(root, text=".", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=210, y=400)
tk.Button(root, text="=", width=4, height=4, font=button_font, bd=1, fg="#fff", bg="#fe9037", command=lambda: calculate()).place(x=310, y=312)

tk.Button(root, text="sin", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#3697f5", command=lambda: show("sin")).place(x=10, y=480)
tk.Button(root, text="cos", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("cos")).place(x=110, y=480)
tk.Button(root, text="tan", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("tan")).place(x=210, y=480)
tk.Button(root, text="log", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("log")).place(x=310, y=480)

tk.Button(root, text="sqrt", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#3697f5", command=lambda: show("sqrt")).place(x=10, y=560)
tk.Button(root, text="(", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("(")).place(x=110, y=560)
tk.Button(root, text=")", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(")")).place(x=210, y=560)
tk.Button(root, text="^", width=4, height=1, font=button_font, bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("^")).place(x=310, y=560)

root.bind("<Key>", key_press)
root.bind("<BackSpace>", handle_backspace)

root.mainloop()

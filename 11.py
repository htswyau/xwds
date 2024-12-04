import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
notebook = ttk.Notebook(root)
text_frame = tk.Frame(notebook)
root.title("Кислицын Владимир")
root.geometry("400x200")
root.resizable(False, False)
notebook.pack(expand=True, fill="both")
calc_tab = tk.Frame(notebook)
notebook.add(calc_tab, text="Калькулятор")
num1_entry = tk.Entry(calc_tab, width=10)
num1_entry.grid(row=1, column=1)
num2_entry = tk.Entry(calc_tab, width=10)
num2_entry.grid(row=1, column=3)
operators = ["+", "-", "*", "/"]
operator_combobox = ttk.Combobox(calc_tab, values=operators)
operator_combobox.grid(row=1, column=2)

def calculate():
  num1 = int(num1_entry.get())
  num2 = int(num2_entry.get())
  operator = operator_combobox.get()
  if operator=='+':
    messagebox.showinfo('Ответ', num1+num2)
  if operator=='-':
    messagebox.showinfo('Ответ', num1-num2)
  if operator=='*':
    messagebox.showinfo('Ответ', num1*num2)
  if operator == '/':
    messagebox.showinfo('Ответ', num1//num2)
calculate_button = tk.Button(calc_tab, text="Вычислить", command=calculate)
calculate_button.grid(row=1, column=4)
checkbox_tab = tk.Frame(notebook)
notebook.add(checkbox_tab, text="Ответы")

def choose():
  a1 = enavled1.get()
  a2 = enavled2.get()
  a3 = enavled3.get()
  if a1==1 and a2==1 and a3==1:messagebox.showinfo('Выбранные варианты', '1 и 2 и 3')
  elif a1==1 and a2==1:messagebox.showinfo('Выбранные варианты', '1 и 2')
  elif a2==1 and a3==1:messagebox.showinfo('Выбранные варианты', '2 и 3')
  elif a1==1 and a3==1:messagebox.showinfo('Выбранные варианты', '1 и 3')
  elif a1 == 1: messagebox.showinfo('Выбранные варианты', '1')
  elif a2 == 1: messagebox.showinfo('Выбранные варианты', '2')
  elif a3 == 1: messagebox.showinfo('Выбранные варианты', '3')


position = {"padx":4, "pady":4,"expand": True, "anchor":SW}
enavled1 = BooleanVar()
checkbox1 = ttk.Checkbutton(checkbox_tab, text="1",variable=enavled1)
checkbox1.pack(position)
enavled2 = BooleanVar()
checkbox2 = ttk.Checkbutton(checkbox_tab, text="2",variable=enavled2)
checkbox2.pack(position)
enavled3 = BooleanVar()
checkbox3 = ttk.Checkbutton(checkbox_tab, text="3",variable=enavled3)
checkbox3.pack(position)
btn_check = Button(checkbox_tab, text='Проверка', command=choose)
btn_check.pack(position)
notebook.add(text_frame, text="Текст")
text_editor = Text(text_frame)
text_editor.pack(fill=BOTH, expand=True)

def open_file():
  filepath = filedialog.askopenfilename()
  if filepath != "":
    with open(filepath, "r") as file:
      text = file.read()
      text_editor.delete("1.0", END)
      text_editor.insert("1.0", text)

def save_file():
  filepath = filedialog.asksaveasfilename()
  if filepath != "":
    text = text_editor.get("1.0", END)
    with open(filepath, "w") as file:
      file.write(text)

open_button = ttk.Button(text_editor,text="Открыть", command=open_file)
open_button.pack(side=LEFT, fill=X, expand=True, padx=10, anchor=SW)

save_button = ttk.Button(text_editor,text="Сохранить", command=save_file)
save_button.pack(side=RIGHT, fill=X, expand=True, padx=10,anchor=SE)

root.mainloop()
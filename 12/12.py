import requests
import json
from tkinter import *
from pprint import pprint

window = Tk()
window.geometry('400x200')
window.title('Кислицын Владимир Александрович')
e = Entry(window, width=10)
e.pack()
l = Label(window, text='Введите никнейм')
l.pack()

def f():
    a = e.get()
    username = a
    url = f"https://api.github.com/users/{username}"
    data = {}
    user_data = requests.get(url).json()
    pprint(user_data)
    key = ['company', 'created_at', 'email', 'id', 'name', 'url']
    for i in key:
        data[i] = user_data.get(i)
    with open('12json.txt', 'w', encoding='utf-8') as rr:
        json.dump(data, rr, ensure_ascii=False, indent=4)

bt = Button(window, text="Подтвердить", command=f, width=30)
bt.pack()
window.mainloop()
with open('12json.txt', 'w') as file_json:
  json.dump(info, file_json)
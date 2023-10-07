import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import pyperclip

class CurrencyConverter:
    def __init__(self, usd_exchange_rate):
        self.usd_exchange_rate = usd_exchange_rate

    def convert_to_usd(self, amount):
        return amount / self.usd_exchange_rate

def get_usd_exchange_rate():
    url = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D1%81%D1%88%D0%B0+%D0%B2+%D1%83%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B5'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        usd_block = soup.find('div', class_='BNeawe iBp4i AP7Wnd')

        if usd_block:
            usd_text = usd_block.text.strip()

            try:
                usd_exchange_rate = float(usd_text.split()[0].replace(',', '.'))
                return usd_exchange_rate
            except ValueError:
                print("Не вдалося перетворити курс валюти в число.")
                return None
        else:
            print("Не вдалося знайти інформацію про курс долара США на сторінці Google.")
            return None
    else:
        print("Не вдалося отримати дані зі сторінки Google.")
        return None

def convert_currency():
    amount_str = amount_entry.get()
    try:
        amount = float(amount_str)
        usd_exchange_rate = get_usd_exchange_rate()
        if usd_exchange_rate:
            converter = CurrencyConverter(usd_exchange_rate)
            result = converter.convert_to_usd(amount)
            result_label.config(text=f"Результат: {result:.2f} USD")
            continue_button.config(state=tk.NORMAL)
            copy_button.config(state=tk.NORMAL)
    except ValueError:
        messagebox.showerror("Помилка", "Некоректний ввід суми")

def continue_conversion():
    amount_entry.delete(0, tk.END)
    result_label.config(text="")
    continue_button.config(state=tk.DISABLED)
    copy_button.config(state=tk.DISABLED)

def copy_result():
    result_text = result_label.cget("text")
    if result_text:
        pyperclip.copy(result_text)

def paste_from_clipboard():
    clipboard_text = pyperclip.paste()
    if clipboard_text:
        amount_entry.delete(0, tk.END)
        amount_entry.insert(0, clipboard_text)

def change_theme(event):
    selected_theme = theme_combobox.get()
    if selected_theme == "Light":
        root.tk_setPalette(background='#ffffff', foreground='#000000')
        frame.config(bg='#ffffff')
        amount_label.config(bg='#ffffff', fg='#000000')
        convert_button.config(bg='#ffffff', fg='#000000')
        continue_button.config(bg='#ffffff', fg='#000000')
        copy_button.config(bg='#ffffff', fg='#000000')
        paste_button.config(bg='#ffffff', fg='#000000')
    elif selected_theme == "Dark":
        root.tk_setPalette(background='#000000', foreground='#ffffff')
        frame.config(bg='#000000')
        amount_label.config(bg='#000000', fg='#ffffff')
        convert_button.config(bg='#000000', fg='#ffffff')
        continue_button.config(bg='#000000', fg='#ffffff')
        copy_button.config(bg='#000000', fg='#ffffff')
        paste_button.config(bg='#000000', fg='#ffffff')

root = tk.Tk()
root.title("Конвертер валюти")
root.geometry("300x300")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

amount_label = tk.Label(frame, text="Введіть кількість вашої валюти:")
amount_label.pack()

amount_entry = tk.Entry(frame)
amount_entry.pack()

convert_button = tk.Button(frame, text="Конвертувати", command=convert_currency)
convert_button.pack()

result_label = tk.Label(frame, text="")
result_label.pack()

continue_button = tk.Button(frame, text="Продовжити", command=continue_conversion, state=tk.DISABLED)
continue_button.pack()

copy_button = tk.Button(frame, text="Copy", command=copy_result, state=tk.DISABLED)
copy_button.pack()

paste_button = tk.Button(frame, text="Paste", command=paste_from_clipboard)
paste_button.pack()

theme_label = tk.Label(frame, text="Виберіть тему:")
theme_label.pack()

themes = ["Light", "Dark"]
theme_combobox = ttk.Combobox(frame, values=themes)
theme_combobox.pack()
theme_combobox.bind("<<ComboboxSelected>>", change_theme)
theme_combobox.set("Light")

root.mainloop()
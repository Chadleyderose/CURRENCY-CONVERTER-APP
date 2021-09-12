import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

url = 'https://api.exchangerate-api.com/v4/latest/USD'

class ConvertNow():
        def __init__(self,response):
            self.data = requests.get(response).json()
            self.currencies = self.data['rates']

        def convert(self, from_currency, to_currency, amount):
            if from_currency != 'USD' :
             amount = amount / self.currencies[from_currency]

            amount = round(amount * self.currencies[to_currency], 4)
            return amount

class GUI(tk.Tk):
        def __init__(self, converter):
            tk.Tk.__init__(self)
            self.title("Currency Converter")
            self.currency_converter = converter
            self.geometry("500x200")

            self.toplabel = Label(self, text = 'Covert your Currency\n to another Currency in \n REAL TIME')
            self.toplabel.place(x = 10 , y = 100)

            font = ("FreeSerif", 12, "bold")

            self.from_currency_var = StringVar(self)
            self.from_currency_var.set("USD")
            self.to_currency_var = StringVar(self)
            self.to_currency_var.set("INR")

            self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_var,values=list
            (self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 15, justify = tk.CENTER)
            self.from_currency_dropdown.place(x = 30,y= 10)

            self.amount_ent = Entry(self,bd = 3,relief = tk.RIDGE, justify = tk.CENTER, width = 17)
            self.amount_ent.place(x = 30, y = 50)

            self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_var,values=list
            (self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 13, justify = tk.CENTER)
            self.to_currency_dropdown.place(x = 250,y= 10)

            self.converted_amount_lbl = Label(self, text = '', fg = 'black', bg = 'white',
            relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)
            self.converted_amount_lbl.place(x = 250, y = 50)

            self.convertbtn = Button(self, text = "Convert",command = self.my_function,width=20,height=2)
            self.convertbtn.place(x=260,y=110)

        def my_function(self):
            amount = float(self.amount_ent.get())
            from_cur = self.from_currency_var.get()
            to_cur = self.to_currency_var.get()

            converted_amount = self.currency_converter.convert(from_cur,to_cur,amount)
            converted_amount = round(converted_amount, 2)
            self.converted_amount_lbl.config(text = str(converted_amount))

converter = ConvertNow(url)
GUI(converter)

mainloop()

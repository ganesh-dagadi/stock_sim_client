import tkinter as tk
from tkinter import StringVar, ttk
import stock_sim_backend as backend
import numpy as np

import Views.Holdings as Holdings
import Views.Home as Home
import Views.Transactions as Transactions


class Account(tk.Frame):
    def __init__(self , parent , controller):
        self.controller = controller
        tk.Frame.__init__(self , parent)
        self.create_widgets()
    
    def create_widgets(self):
        try:
            account_data = backend.get_account_info()
            total_holding_val = backend.get_total_holding_value()

            self.entered_amt = StringVar()

            title_label = ttk.Label(self , text = "My Account" , font=('TkDefaultFont', 30))
            title_label.grid(row = 0 , columnspan=5 , padx=300 , pady=10 , sticky=tk.W+tk.E)

            balance_label = ttk.Label(self , text="Balance :" , font=('TkDefaultFont' , 15))
            balance_label.grid(row = 1 , column=1 , pady=20 )
            balance_val = ttk.Label(self , text=str(np.round(float(account_data['balance']) , 2)) , font=('TkDefaultFont' , 15))
            balance_val.grid(row = 1 , column=2 , pady=20 )

            #Add amount
            add_amt_label = ttk.Label(self , text="Add amount :" , font=('TkDefaultFont' , 15))
            add_amt_label.grid(row = 2 , column=1 , pady=20 )
            add_amt_entry = ttk.Entry(self , textvariable=self.entered_amt , font=('TkDefaultFont' , 15))
            add_amt_entry.grid(row = 2 , column=2 , pady=20 )

            add_amt_button = ttk.Button(self , text="Add" , command=self.handle_add_amount)
            add_amt_button.grid(row=3 ,columnspan=5 , pady=20)

            total_amt_label = ttk.Label(self , text="Total amount added :" , font=('TkDefaultFont' , 15))
            total_amt_label.grid(row = 4 , column=1 , pady=20 )
            total_amt_val = ttk.Label(self , text=str(np.round(float(account_data['total_income']) , 2)) , font=('TkDefaultFont' , 15))
            total_amt_val.grid(row = 4 , column=2 , pady=20 )

            total_holding_label = ttk.Label(self , text="Total Holdings value :" , font=('TkDefaultFont' , 15))
            total_holding_label.grid(row = 5 , column=1 , pady=20 )
            total_holding_val_label = ttk.Label(self , text=str(np.round(float(total_holding_val) , 2)) , font=('TkDefaultFont' , 15))
            total_holding_val_label.grid(row = 5 , column=2 , pady=20 )

            profit = (float(account_data['balance']) + float(total_holding_val)) - float(account_data['total_income']) 
            profit_label = ttk.Label(self , text="Total Profit :" , font=('TkDefaultFont' , 15))
            profit_label.grid(row = 6 , column=1 , pady=20 )
            profit_val = ttk.Label(self , text=str(np.round(profit, 2)) , font=('TkDefaultFont' , 15))
            profit_val.grid(row = 6 , column=2 , pady=20 )

            res_label = ttk.Label(self , text='')
            res_label.grid(row=7 , columnspan=5 , pady=10)

            transac_button = ttk.Button(self , text="View transactions" , command=lambda:self.controller.show_page(Transactions.Transactions))
            transac_button.grid(row=8 , column=0 , pady=10)

            Home_button = ttk.Button(self , text="Home" , command=lambda:self.controller.show_page(Home.HomeView))
            Home_button.grid(row=8 , column=1 , pady=10)

            Holdings_button = ttk.Button(self , text="View Holdings" , command=lambda:self.controller.show_page(Holdings.Holdings))
            Holdings_button.grid(row=8 , column=4 , pady=10)

            self.res_label = res_label

        except Exception as e:
            print(e)

    def handle_add_amount(self):
        try:
            entered_amt = self.entered_amt.get()
            if(len(entered_amt) == 0):
                raise Exception("Cant add 0 to account")

            entered_amt = float(entered_amt)
            if(entered_amt < 0.0):
                raise Exception("Cant add -ve amount")
            res = backend.add_amt_acc(entered_amt)
            self.res_label['text'] = res
            self.controller.show_page(Account)
        except Exception as e:
            self.res_label['text'] = e
        

import tkinter as tk
from tkinter import ttk
import Views.Home as Home
import Views.Stock_dispg as Stock_dispg
import stock_sim_backend.server_endpoints.account_info as ai
import stock_sim_backend.server_endpoints.stock_info as si
import stock_sim_backend.server_endpoints.transactions as tr
import numpy as np

class Stock_buypg(tk.Frame):
    def __init__(self , parent , controller):
        self.controller = controller
        tk.Frame.__init__(self , parent)
        self.bind("<<ShowFrame>>" , self.display_stock_info)
        self.create_widgets()
    
    def create_widgets(self):
        try:
            acc_bal = ai.get_account_info()['balance']
            acc_bal = np.round(float(acc_bal) , 2)
            ticker_name_label = ttk.Label(self, text="text", wraplength=600, font=(
                "TkDefaultFont", 20))
            ticker_name_label.grid(row=0, columnspan=5, padx=300,
                                   pady=10, sticky=tk.E+tk.W)
            
            acc_bal_label = ttk.Label(
                self, text="Balance : "+str(acc_bal), font=('TKDefaultFont',15))
            acc_bal_label.grid(row=1, column=1, padx=0, sticky=tk.W)
            unit_price_label = ttk.Label(self, text="Unit Price : ", font=('TKDefaultFont' ,15))
            unit_price_label.grid(row=2, column=2, padx=0, pady=30)
            stock_price_label = ttk.Label(self, text='Price', font=('TKDefaultFont',15))
            stock_price_label.grid(row=2, column=3, pady=30)
            
            qty_label = ttk.Label(self, text='Qty', font=('TKDefaultFont',15))
            qty_label.grid(row=3, column=2, pady=10)
            self.qty_entered = tk.StringVar()
            qty_entry = ttk.Entry(self, font=('TKDefaultFont',15) , textvariable=self.qty_entered)
            qty_entry.grid(row=3, column=3, pady=10, sticky=tk.W)
            qty_entry.bind('<KeyRelease>' , self.calculate_total)

            total_label = ttk.Label(self, text="Total Price : ", font=('TKDefaultFont',15))
            total_label.grid(row=4, column=2, padx=0, pady=30)
            total_price_label = ttk.Label(self, text='0', font=('TKDefaultFont',15))
            total_price_label.grid(row=4, column=3, pady=30)
            

            confirm_button = ttk.Button(self , text="Confirm" , command= self.handle_confirm_buy)
            confirm_button.grid(row=5 , columnspan= 5 , pady=20)

            cancel_button = ttk.Button(self , text="Cancel" , command= lambda:self.controller.show_page(Stock_dispg.Stock_dispg))
            cancel_button.grid(row=6 , columnspan= 5 , pady=20)
            
            res_label = ttk.Label(self , text='')
            res_label.grid(row=7 , columnspan=5 , pady=20)
            home_return_button = ttk.Button(self, text="Home",
                                        command=lambda: self.controller.show_page(Home.HomeView))
            home_return_button.grid(row=8, columnspan=5, pady=20, sticky=tk.S)
            #Setting widgets to self
            self.res_label = res_label
            self.ticker_name_label = ticker_name_label
            self.stock_price_label = stock_price_label
            self.total_price_label = total_price_label
            self.confim_button = confirm_button
        except Exception as e:
            print(e)

    def display_stock_info(self, event):  
        try:
            selected_ticker = self.controller.app_data['Selected_ticker_buy'].get()
            live_price = np.round(float(si.get_live_price(selected_ticker)) , 2)
            self.ticker_name_label['text'] = selected_ticker
            self.stock_price_label['text'] = str(live_price)
        except Exception as e:
            self.res_label['text'] = e
    def calculate_total(self , event):
        try:
            qty = self.qty_entered.get()
            if(len(qty) ==0):
                qty = '0'
            if('.' in qty):
                raise Exception("Qty must be a whole number")

            if(not qty.isdigit()):
                raise Exception("qty must be a number")
            
            
            total = float(self.stock_price_label['text']) * int(qty)
            total = np.round(total , 2)
            self.total_price_label['text'] = str(total)
        except Exception as e:
            self.res_label['text'] = e
            

    def handle_confirm_buy(self):
        try:
            qty = self.qty_entered.get()
            if(len(qty) ==0):
               raise Exception("Minimum buy quantity is 1")
            if('.' in qty):
                raise Exception("Qty must be a whole number")

            if(not qty.isdigit()):
                raise Exception("qty must be a number")
            response = tr.buy_stock(self.controller.app_data['Selected_ticker_buy'].get() , int(qty))
            res_label = ttk.Label(self , text=response)
            res_label.grid(row=6 , columnspan=5 , pady=20)
            self.confim_button['state'] = "disabled"
        except Exception as e:
           self.res_label['text'] = e
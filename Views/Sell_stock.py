import tkinter as tk
from tkinter import ttk
import stock_sim_backend.server_endpoints.stock_info as si
import stock_sim_backend.server_endpoints.account_info as ai
import stock_sim_backend.server_endpoints.transactions as tr
import numpy as np
import Views.Home as Home
import Views.Holdings as Holdings

class Sell_stock(tk.Frame):
    def __init__(self , parent , controller):
        self.controller = controller
        tk.Frame.__init__(self , parent)
        self.bind('<<ShowFrame>>' , self.display_stock_data)
        self.create_widgets()
    
    def create_widgets(self):
        try:
            selected_ticker = self.controller.app_data['Selected_ticker_sell'].get()
            live_price = np.round(float(si.get_live_price(selected_ticker)) , 2)
            title_label = ttk.Label(self , text=f"SELL {selected_ticker}" ,font=('TKDefaultFont' , 30))
            title_label.grid(row = 0 , columnspan = 5 , padx=300 , pady=10 , sticky=tk.W+tk.E)
            #Live price
            live_label = ttk.Label(self , text="Live price" , font=('TKDefaultFont' , 12))
            live_label.grid(row=2 , column=2 , padx = 30 ,pady=20)

            live_price = ttk.Label(self , text=live_price , font=('TKDefaultFont' , 12))
            live_price.grid(row=2 , column=3 , padx=30, pady=20)

            qty_label = ttk.Label(self, text='Quantity', font=('TKDefaultFont',12))
            qty_label.grid(row=3, column=2, pady=10)
            self.qty_entered = tk.StringVar()
            qty_entry = ttk.Entry(self, font=('TKDefaultFont' ,12) , textvariable=self.qty_entered)
            qty_entry.grid(row=3, column=3, pady=10, sticky=tk.W)
            qty_entry.bind('<KeyRelease>' , self.calculate_total)

            total_label = ttk.Label(self, text="Total Price : ", font=('TKDefaultFont' , 12))
            total_label.grid(row=4, column=2, padx=0, pady=20)
            total_price_label = ttk.Label(self, text='0', font=('TKDefaultFont',12))
            total_price_label.grid(row=4, column=3, pady=20)

            #Current holding
            curr_hold = ai.get_one_holding(selected_ticker)
            current_label = ttk.Label(self , text="Current Holding" , font=('TkDefaultFont' , 15))
            current_label.grid(row=5 , columnspan=5 , pady=20)
            
            unit_prc_label = ttk.Label(self , text="Unit Price" , font=('TkDefaultFont' , 12))
            unit_prc_label.grid(row=6 , column=2 , pady=10)

            unit_prc = ttk.Label(self , text=str(np.round(float(curr_hold['unit_price']) , 2)) , font=('TkDefaultFont' , 12))
            unit_prc.grid(row=6 , column=3 , pady=10)

            qty_label = ttk.Label(self , text="Quantity" , font=('TkDefaultFont' , 12))
            qty_label.grid(row=7 , column=2 , pady=10)

            qty_val = ttk.Label(self , text=str(curr_hold['qty']) , font=('TkDefaultFont' , 12))
            qty_val.grid(row=7 , column=3 , pady=10)

            profit_label = ttk.Label(self , text="Profit" , font=('TkDefaultFont' , 12))
            profit_label.grid(row=8 , column=2 , pady=10)

            profit_val = ttk.Label(self , text="" , font=('TkDefaultFont' , 12))
            profit_val.grid(row=8 , column=3 , pady=10)

            confirm_button = ttk.Button(self , text="Confirm" , command= self.handle_confirm_sell)
            confirm_button.grid(row=9 , columnspan= 5 , pady=10)

            cancel_button = ttk.Button(self , text="Cancel" , command= lambda:self.controller.show_page(Holdings.Holdings))
            cancel_button.grid(row=10 , columnspan= 5 , pady=10)
            
            res_label = ttk.Label(self , text='')
            res_label.grid(row=11 , columnspan=5 , pady=10)
            home_return_button = ttk.Button(self, text="Home",
                                        command=lambda: self.controller.show_page(Home.HomeView))
            home_return_button.grid(row=12, columnspan=5, pady=10, sticky=tk.S)
            #Setting required widgets to self
            self.res_label = res_label
            self.curr_hold = curr_hold
            self.profit_val = profit_val
            self.total_price_label = total_price_label
            self.live_price = live_price
        except Exception as e:
            print(e)
    def display_stock_data(self , event):
        pass

    def calculate_total(self , event):
        try:
            qty = self.qty_entered.get()
            curr_hold = self.curr_hold
            if(len(qty) ==0):
                qty = '0'
            if('.' in qty):
                raise Exception("Qty must be a whole number")

            if(not qty.isdigit()):
                raise Exception("qty must be a number")
            if(int(qty) > curr_hold['qty']):
                raise Exception("You cant sell more than you own")
           
            
            
            total = float(self.live_price['text']) * int(qty)
            total = np.round(total , 2)
            self.total_price_label['text'] = str(total)

            #Calculate profit to update profit label
            total_live_cost = float(self.live_price['text']) * int(qty)
            total_holding_cost = float(curr_hold['unit_price']) * int(qty)
            profit = total_live_cost-total_holding_cost
            profit = np.round(profit , 2)
            self.profit_val['text'] = str(profit)
        except Exception as e:
            # print(e)
            self.res_label['text'] = e
    def handle_confirm_sell(self):
        try:
            qty = self.qty_entered.get()
            curr_hold = self.curr_hold
            if(len(qty) ==0):
                qty = '0'
            if('.' in qty):
                raise Exception("Qty must be a whole number")

            if(not qty.isdigit()):
                raise Exception("qty must be a number")

            if(int(qty) > curr_hold['qty']):
                raise Exception("You cant sell more than you own")
            
            res = tr.sell_stock(self.curr_hold['ticker'] , int(self.qty_entered.get()))
            self.res_label['text'] = res
        except Exception as e:
            self.res_label['text'] = e


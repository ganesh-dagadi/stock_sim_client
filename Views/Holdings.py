import tkinter as tk
from tkinter import CENTER, ttk
import numpy as np
import stock_sim_backend.server_endpoints.account_info as ai
import Views.Home as Home
import Views.Sell_stock as Sell_stock

class Holdings(tk.Frame):
    def __init__(self , parent , controller):
        self.controller = controller
        tk.Frame.__init__(self , parent)
        self.bind('<<ShowFrame>>' , self.display_holdings_data)
        self.create_widgets()

    def create_widgets(self):
        try:
            #Get required data from backend
            total_holding_val = np.round(float(ai.get_total_holding_value()) , 2)
            #Render the widgets
            title_label = ttk.Label(self , text="My Holdings" , font=(
            "TkDefaultFont", 30))
            title_label.grid(row=0 , column = 0 , padx=50)
            holdings_tree = ttk.Treeview(self , columns=('ticker' , 'name' , 'unit_price' , 'qty' , 'total'), show="headings" , height=12)
            holdings_tree.grid(row = 1, column=0 , pady=10 , padx=50)
            holdings_tree.column('ticker' , anchor=CENTER , width=80)
            holdings_tree.column('name' , anchor=CENTER , width=350)
            holdings_tree.column('unit_price' , anchor=CENTER , width=80)
            holdings_tree.column('qty' , anchor=CENTER , width=80)
            holdings_tree.column('total' , anchor=CENTER , width=80)

            holdings_tree.heading('ticker' , text='Ticker')
            holdings_tree.heading('name' , text='Name')
            holdings_tree.heading('unit_price' , text='Unit Price')
            holdings_tree.heading('qty' , text='Quantity')
            holdings_tree.heading('total' , text='Total')

            total_label = ttk.Label(self , text="Total Holdings Value" , font=('TkDefaultFont' , 18))
            total_label.grid(row = 2 , column=0 , padx=250 , pady=8)
            total_val_label = ttk.Label(self , text = str(total_holding_val) , font=('TkDefaultFont' , 15))
            total_val_label.grid(row = 3 , column=0 , padx=170 , pady=8)

            sell_info_label = ttk.Label(self , text="Select a stock and click on sell to sell the stock" , font=('TkDefaultFont' , 12))
            sell_info_label.grid(row=4 , column=0, padx=170 , pady=8)

            sell_button = ttk.Button(self , text="SELL" , command = self.handle_sell_click)
            sell_button.grid(row=5 , column=0, padx=250)

            home_button = ttk.Button(self , text="Home" , command=lambda:self.controller.show_page(Home.HomeView))
            home_button.grid(row=6 , column=0 , padx=150 , pady=10)
             #Set widgets to self
            self.holdings_tree = holdings_tree
        except Exception as e:
            print(e)
       
    def display_holdings_data(self , event):
        try:
            holdings = ai.get_all_holdings()
            modified_holdings = []
            for i in holdings:
                unit_price = np.round(float(i['unit_price']) , 2)
                qty = i['qty']
                total = unit_price * qty
                total = np.round(total , 2)
                sub_list = [i['ticker'] , i['stock_name'] , str(unit_price) , str(qty) , str(total)]
                modified_holdings.append(sub_list)

            for i in modified_holdings:
                self.holdings_tree.insert('' , index='end' , values=i)
        except Exception as e:
            print(e)
    def handle_sell_click(self):
        cur_item = self.holdings_tree.focus()
        ticker = self.holdings_tree.item(cur_item)['values'][0]
        self.controller.app_data['Selected_ticker_sell'].set(ticker)
        self.controller.show_page(Sell_stock.Sell_stock)
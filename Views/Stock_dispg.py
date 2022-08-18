import tkinter as tk
from tkinter import ttk
import stock_sim_backend as backend
import matplotlib.pyplot as plt
import numpy as np
import Views.Home as Home
import Views.Stock_buypg as Stock_buypg

class Stock_dispg(tk.Frame):
    def __init__(self , parent , controller):
        self.controller = controller
        tk.Frame.__init__(self , parent)
        self.bind('<<ShowFrame>>' , self.display_stock_info)
        self.create_widgets()
    
    def create_widgets(self):
        try:
            ticker_name_label = ttk.Label(self, text="text", wraplength=600, font=(
                "TkDefaultFont", 20))
            ticker_name_label.grid(row=0, columnspan=7, padx=300,
                                    pady=10, sticky=tk.E+tk.W)
            acc_bal = backend.get_account_info()['balance']
            acc_bal = np.round(float(acc_bal) , 2)
            ticker_name_label = ttk.Label(self, text="text", wraplength=600, font=(
                    "TkDefaultFont", 20))
            ticker_name_label.grid(row=0, columnspan=7, padx=300,
                                    pady=10, sticky=tk.E+tk.W)
            self.ticker_name_label = ticker_name_label
            stock_price_label = ttk.Label(
                    self, text="0", font=(15))
            stock_price_label.grid(row=1, columnspan=7, pady=20,
                                    padx=300, sticky=(tk.E+tk.W))
            self.stock_price_label = stock_price_label

            stock_price_graph_label = ttk.Label(
                self, text='Pricegraph :', font=(15))
            stock_price_graph_label.grid(row=2, columnspan=7, pady=10,
                                         padx=300, sticky=(tk.E+tk.W))
            stock_select_duration_label = ttk.Label(
                self, text='Select duration:', font=(15))
            stock_select_duration_label.grid(row=3, columnspan=7, pady=10,
                                             padx=300, sticky=(tk.E+tk.W))

            #Duration buttons

            stock_7D_button = ttk.Button(
                self, text='7D', command=lambda: self.disp_price_graph(7))
            stock_7D_button.grid(row=4, column=0, pady=10)
            stock_14D_button = ttk.Button(
                self, text='14D', command=lambda: self.disp_price_graph(14))
            stock_14D_button.grid(row=4, column=1, pady=10)
            stock_1M_button = ttk.Button(
                self, text='1M', command=lambda: self.disp_price_graph(30))
            stock_1M_button.grid(row=4, column=2, pady=10)
            stock_6M_button = ttk.Button(
                self, text='6M', command=lambda: self.disp_price_graph(180))
            stock_6M_button.grid(row=4, column=3, pady=10)
            stock_1Y_button = ttk.Button(
                self, text='1Y', command=lambda: self.disp_price_graph(365))
            stock_1Y_button.grid(row=5, column=1, pady=10)
            stock_5Y_button = ttk.Button(
                self, text='5Y', command=lambda: self.disp_price_graph(1825))
            stock_5Y_button.grid(row=5, column=2, pady=10)
            stock_MAX_button = ttk.Button(
                self, text='MAX', command=lambda: self.disp_price_graph('max'))
            stock_MAX_button.grid(row=5, column=3, pady=10)

            #From buy button

            stock_buy_button = ttk.Button(
                self, text='BUY', command= self.handle_buy)
            stock_buy_button.grid(row=6, columnspan=7,
                                  sticky=tk.W+tk.E, pady=20, padx=300)
            stock_balance_label = ttk.Label(
                self, text="Balance : "+str(acc_bal))
            stock_balance_label.grid(
                row=7, columnspan=7, sticky=tk.W+tk.E, pady=10, padx=300)
            home_button = ttk.Button(
                self, text="Home", command=lambda: self.controller.show_page(Home.HomeView))
            home_button.grid(row=8, columnspan=7,
                             sticky=tk.W+tk.E, pady=30, padx=300)

        except Exception as e:
            print(e)
    
    def display_stock_info(self, event):
        try:
            selected_ticker = self.controller.app_data['Selected_ticker_info'].get()
            live_price = backend.get_live_price(selected_ticker)
            live_price = np.round(float(live_price) , 2)
            self.ticker_name_label['text'] = selected_ticker
            self.stock_price_label['text'] = "Price : "+str(live_price)
        except Exception as e:
            print(e)
      
    def disp_price_graph(self, duration):
        try:
            selected_ticker = self.controller.app_data['Selected_ticker_info'].get()
            graph_data = backend.get_historic_data(selected_ticker, duration)
            plt.plot(graph_data)
            plt.show()
        except Exception as e:
            print(e)
    def handle_buy(self):
        self.controller.app_data['Selected_ticker_buy'].set(self.controller.app_data['Selected_ticker_info'].get())
        self.controller.show_page(Stock_buypg.Stock_buypg)
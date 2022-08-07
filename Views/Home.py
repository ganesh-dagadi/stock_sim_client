import tkinter as tk
from tkinter import ttk
import Views.Search_Result as Search_Result
import Views.Holdings as Holdings
import Views.Account as Account
import stock_sim_backend.server_endpoints.account_info as ai
import numpy as np


class HomeView(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.create_widgets()

    def create_widgets(self):
        try:
            acc_bal = ai.get_account_info()['balance']
            acc_bal = np.round(float(acc_bal) , 2)
            home_page_label = ttk.Label(self, text='Stock Sim', font=(
            "TkDefaultFont", 30), wraplength=600)
            home_page_label.grid(row=0, column=0, padx=300, pady=10)

            search_label = ttk.Label(
                self, text="Search for stock", font=("TkDefaultFont", 15))
            search_label.grid(row=1, column=0, padx=300, pady=10)
            stock_name_entry = ttk.Entry(
                self, textvariable=self.controller.app_data['Search_str'], font=(12))
            stock_name_entry.grid(row=2, column=0,
                                padx=50, columnspan=1, sticky=tk.E+tk.W, pady=10)
            button_Search = ttk.Button(
                self, text="Search", command=self.handle_search_click)
            button_Search.grid(row=4, column=0, pady=10)
            acc_balance_label = ttk.Label(
                self, text=f"Account Balance : {acc_bal}", font=("TkDefaultFont", 10))
            acc_balance_label.grid(row=5, column=0, padx=300)
            more_button = ttk.Button(
                self, text='My account', command=lambda: self.controller.show_page(Account.Account))
            more_button.grid(row=6, column=0, padx=15, sticky=tk.W)
            holdings_button = ttk.Button(
                self, text='Holdings', command=lambda: self.controller.show_page(Holdings.Holdings))
            holdings_button.grid(row=6, column=0, sticky=tk.E)
        except Exception as e:
            print(e)

    def handle_search_click(self):
        self.controller.show_page(Search_Result.SearchResult)
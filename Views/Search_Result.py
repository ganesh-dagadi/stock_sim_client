import tkinter as tk
from tkinter import CENTER, ttk
import Views.Home as Home
import Views.Stock_dispg as Stock_dispg
import stock_sim_backend.server_endpoints.stock_info as si

class SearchResult(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.bind("<<ShowFrame>>", self.get_search_data)
        self.create_widgets()

    def create_widgets(self):

        search_result_label = ttk.Label(self, text='Results', wraplength=600, font=(
            "TkDefaultFont", 30))
        search_result_label.grid(
            row=1, column=0, padx=300, pady=10, sticky=tk.E+tk.W)

        label1 = ttk.Label(
            self, text='Select a stock to view more', font=("TkDefaultFont", 15))
        label1.grid(row=2, column=0, padx=40, pady=10, sticky=tk.W)
        home_return_button = ttk.Button(self, text="Home",
                                        command=lambda: self.controller.show_page(Home.HomeView))
        home_return_button.grid(row=4, column=0, pady=20, sticky=tk.S)

    def get_search_data(self, event):
        try:
            search_string = self.controller.app_data['Search_str'].get()
            if len(search_string) == 0:
                label_error = ttk.Label(
                    self, text="The searched entry cannot be empty, please return to homepage")
                label_error.grid(row=3, column=0, padx=300)
            else:
                data = si.search_stocks(search_string)
                modified_data = []
                for i in data:
                    sub_modified_list = [i['symbol'], i['name']]
                    modified_data.append(sub_modified_list)

                search_res = ttk.Treeview(self, columns=(
                    'symbol', 'name'), show='headings' , height=15)
                search_res.column('symbol', anchor=CENTER, width=80)
                search_res.column('name', anchor=CENTER, width=400)

                search_res.heading('symbol', text="Symbol")
                search_res.heading('name', text="Name")
                for i in modified_data:
                    search_res.insert('', index='end', values=i)
                search_res.grid(row=3, column=0, padx=100, sticky=tk.E + tk.W)
                self.search_res = search_res
                search_res.bind('<ButtonRelease-1>' , self.handle_stock_select)

        except Exception as e:
            print(e)
    
    def handle_stock_select(self , event):
        curItem = self.search_res.focus()
        selected_ticker = self.search_res.item(curItem)['values'][0]
        self.controller.app_data['Selected_ticker_info'].set(selected_ticker)
        self.controller.show_page(Stock_dispg.Stock_dispg)

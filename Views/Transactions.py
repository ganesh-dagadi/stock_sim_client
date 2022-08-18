import tkinter as tk
from tkinter import CENTER, ttk
import stock_sim_backend as backend
import Views.Account as Account

def clean_stck_transac_data(data):
    modified_data = []
    for i in data:
        sub_lst = [str(i['stck_transac_id']) , i['trans_type'] ,i['on_ticker'] , str(i['unit_price']) , str(i['qty']) , str(i['profit']) , str(i['on_time']) , str(i['on_date'])]
        modified_data.append(sub_lst)
    return modified_data
def clean_acc_transac_data(data):
    modified_data = []
    for i in data:
        sub_lst = [str(i['acc_transac_id']) , str(i['amount']) , str(i['on_date']) , str(i['at_time'])]
        modified_data.append(sub_lst)
    return modified_data


class Transactions(tk.Frame):
    def __init__(self , parent , controller):
        self.controller = controller
        tk.Frame.__init__(self , parent)
        self.create_widgets()
    
    def create_widgets(self):
        try:
            transac_data = backend.get_all_transactions()
            stock_transactions =transac_data['stck_transac']
            acc_transactions = transac_data['acc_transac']
            stock_transactions = clean_stck_transac_data(stock_transactions)
            acc_transactions = clean_acc_transac_data(acc_transactions)
            del transac_data

            stck_transac_label = ttk.Label(self , text = "Stock transaction" , font=('TKDEFAULTFONT' , 20))
            stck_transac_label.grid(row = 0 , column=0 , pady = 10 , padx=200)
            stck_transac_tv = ttk.Treeview(self , columns=('transac_id' , 'transac_type' , 'ticker','unit_price' , 'qty' , 'profit' , 'on_time' , 'on_date') , show='headings' , height=10)
            stck_transac_tv.column('transac_id' , anchor=CENTER , width=60)
            stck_transac_tv.column('transac_type' , anchor=CENTER , width=60)
            stck_transac_tv.column('ticker' , anchor=CENTER , width=80)
            stck_transac_tv.column('unit_price' , anchor=CENTER , width=100)
            stck_transac_tv.column('qty' , anchor=CENTER , width=100)
            stck_transac_tv.column('profit' , anchor=CENTER , width=100)
            stck_transac_tv.column('on_time' , anchor=CENTER , width=130)
            stck_transac_tv.column('on_date' , anchor=CENTER , width=110)

            stck_transac_tv.heading('transac_id' , text="Transaction Id")
            stck_transac_tv.heading('transac_type' , text="Type")
            stck_transac_tv.heading('ticker' , text="Ticker")
            stck_transac_tv.heading('unit_price' , text="Unit Price")
            stck_transac_tv.heading('qty' , text="Quantity")
            stck_transac_tv.heading('profit' , text="Profit")
            stck_transac_tv.heading('on_time' , text="Time")
            stck_transac_tv.heading('on_date' , text="Date")

            for i in stock_transactions:
                stck_transac_tv.insert('' , index='end' , values=i)
            stck_transac_tv.grid(row=1 , column=0 , pady=10 , padx=20)

            acc_transac_label = ttk.Label(self , text = "Account transactions" , font=('TKDEFAULTFONT' , 20))
            acc_transac_label.grid(row = 2 , column=0 , pady = 10 , padx=200)
            acc_transac_tv = ttk.Treeview(self , columns=('transac_id' , 'amount' , 'on_date' , 'at_time') , show='headings' , height=8)
            acc_transac_tv.column('transac_id' , anchor=CENTER , width=150)
            acc_transac_tv.column('amount' , anchor=CENTER , width=150)
            acc_transac_tv.column('on_date' , anchor=CENTER , width=150)
            acc_transac_tv.column('at_time' , anchor=CENTER , width=150)

            acc_transac_tv.heading('transac_id' , text="Transaction id")
            acc_transac_tv.heading('amount' , text="Amount")
            acc_transac_tv.heading('on_date' , text="Date")
            acc_transac_tv.heading('at_time' , text="Time")

            for i in acc_transactions:
                acc_transac_tv.insert('' , index='end' , values=i)
            acc_transac_tv.grid(row=3 , column=0 , pady=10 , padx=30)

            home_btn = ttk.Button(self , text="Account" , command=lambda:self.controller.show_page(Account.Account))
            home_btn.grid(row = 5 , column=0 , padx=200 , pady=10)
        except Exception as e:
            print(e)
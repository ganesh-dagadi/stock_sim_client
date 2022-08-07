import tkinter as tk
import setup

setup.setup()

import Views.Home as Home



class Main_window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Stock Simulator")
        self.geometry("800x600")
        self.resizable(width=False, height=False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        container = tk.Frame(self)
        container.grid(column=0, row=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.container = container
        self.app_data = {
            "Search_str": tk.StringVar() ,
            "Selected_ticker_buy" : tk.StringVar(),
            "Selected_ticker_sell" : tk.StringVar(),
            "Selected_ticker_info" : tk.StringVar()
            }
        self.frames = {}
        self.columnconfigure(0, weight=1)
        self.show_page(Home.HomeView)

    def show_page(self, cont):
        frame = cont(self.container , controller = self)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")
       
app = Main_window()
app.mainloop()
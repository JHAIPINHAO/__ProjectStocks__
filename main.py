import datasource
import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import askstring

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
        self.command_menu = tk.Menu(self.menubar)
        self.command_menu.add_command(label="搜尋", command=self.Menu_Search)
        self.menubar.add_cascade(label="證券關鍵字搜尋", menu=self.command_menu)

        MainFrame = ttk.Frame(self)
        MainFrame.pack(padx=50,pady=50)

        TopFrame = ttk.LabelFrame(MainFrame,text=f"各證券收盤價")
        TopFrame.pack()

        columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9')
        self.tree = ttk.Treeview(TopFrame, columns=columns, show='headings')
        self.tree.heading('#1', text='證券代號')
        self.tree.column("#1", minwidth=0, width=100)
        self.tree.heading('#2', text='證券名稱')
        self.tree.column("#2", minwidth=0, width=200)
        self.tree.heading('#3', text='成交股數')
        self.tree.column("#3", minwidth=0, width=100)
        self.tree.heading('#4', text='開盤價')
        self.tree.column("#4", minwidth=0, width=100)
        self.tree.heading('#5', text='最高價')
        self.tree.column("#5", minwidth=0, width=100)
        self.tree.heading('#6', text='最低價')
        self.tree.column("#6", minwidth=0, width=100)
        self.tree.heading('#7', text='收盤價')
        self.tree.column("#7", minwidth=0, width=100)
        self.tree.heading('#8', text='漲跌價差')
        self.tree.column("#8", minwidth=0, width=100)
        self.tree.heading('#9', text='成交筆數')
        self.tree.column("#9", minwidth=0, width=100)
        self.tree.pack(side=tk.LEFT)

        for item in datasource.data_list:
            self.tree.insert('',tk.END,values=[item['證券代號'],item['證券名稱'],item['成交股數'],item['開盤價'],item['最高價'],item['最低價'],item['收盤價'],item['漲跌價差'],item['成交筆數']])

        Scrollbar = ttk.Scrollbar(TopFrame,command=self.tree.yview)
        Scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        self.tree.config(yscrollcommand=Scrollbar.set)

    def Menu_Search(self):
        stock_str = askstring("查詢證券名","請輸入證券關鍵字") 

        for child in self.tree.get_children():
            self.tree.delete(child)

        for item in datasource.data_list:
            if stock_str in (item['證券代號']) or stock_str in (item['證券名稱']):
                self.tree.insert('',tk.END,values=[item['證券代號'],item['證券名稱'],item['成交股數'],item['開盤價'],item['最高價'],item['最低價'],item['收盤價'],item['漲跌價差'],item['成交筆數']])

def main():
    windows = Window()
    windows.title('個股日成交資訊')
    windows.mainloop()

if __name__=='__main__':
    main()
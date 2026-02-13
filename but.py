"""
Simple demo of accent button widget
"""
from tkinter import *
from tkinter import ttk
import TKinterModernThemes as TKMT
import tkinter as tk


class App(TKMT.ThemedTKinterFrame):
    def __init__(self, theme="park", mode="dark", usecommandlineargs=True, usethemeconfigfile=True):
        super().__init__("Sergonizer Pro", theme, mode,
                         usecommandlineargs=usecommandlineargs, useconfigfile=usethemeconfigfile)
        self.root.iconbitmap(default="pro.ico")

        self.checkbox1 = tk.BooleanVar()
        self.checkbox2 = tk.BooleanVar(value=True)
        self.key_textvar_ih = tk.StringVar(value="13")
        self.sn_textvar_ih = tk.StringVar()

        # windows
        self.paned_window = self.PanedWindow("Paned Window Test", padx=1)
        self.paned_window_1 = self.PanedWindow("Paned Window Test", col=2, padx=1)
        self.pane2 = self.paned_window.addWindow()
        self.pane3 = self.paned_window.addWindow()
        self.pane1 = self.paned_window_1.addWindow()

        # Tabs
        self.notebook_r = self.pane1.Notebook("Test Notebook")
        self.notebook = self.pane2.Notebook("Test Notebook")

        self.tab_1 = self.notebook.addTab("Валюты 1")
        self.tab_2 = self.notebook.addTab("Валюты 2")
        self.tab_2.Label("Label text here.")
        self.tab_3 = self.notebook.addTab("Свои валюты")
        self.tab_3.Text("Normal text here.")
        self.add_currency = self.notebook.addTab("Добавить валюту")
        self.ih110_iv = self.notebook_r.addTab("IH110 - IV")
        self.ih110_if = self.notebook_r.addTab("IH110 - IF")
        self.magner = self.notebook_r.addTab("Magner 175")

        # IV 110 tab
        self.ih110_iv.Text("Ключ шифрования", pady=1)
        self.ih110_iv.Entry(self.key_textvar_ih, validatecommand=self.validate_text, pady=1, widgetkwargs={"width": 35})
        self.ih110_iv.Text("Серийный номер", pady=1)
        self.ih110_iv.Entry(self.sn_textvar_ih, validatecommand=self.validate_text, pady=1, widgetkwargs={"width": 35})
        self.ih110_iv.AccentButton("Создать файл", self.make_file)

        # IF 110 tab
        self.ih110_if.Text("Ключ шифрования", pady=1)
        self.ih110_if.Entry(self.key_textvar_ih, validatecommand=self.validate_text, pady=1, widgetkwargs={"width": 35})
        self.ih110_if.Text("Серийный номер", pady=1)
        self.ih110_if.Entry(self.sn_textvar_ih, validatecommand=self.validate_text, pady=1, widgetkwargs={"width": 35})
        self.ih110_if.AccentButton("Создать файл", self.make_file)
        self.ih110_if.Text("\t!!!Внимание!!!\nДанная модель не тестировалась", pady=10, sticky="s")

        # Magner 175
        self.magner.Text("Ключ шифрования", pady=1)
        self.magner.Entry(self.key_textvar_ih, validatecommand=self.validate_text, pady=1, widgetkwargs={"width": 35})
        self.magner.Text("Серийный номер", pady=1)
        self.magner.Entry(self.sn_textvar_ih, validatecommand=self.validate_text, pady=1, widgetkwargs={"width": 35})
        self.magner.AccentButton("Создать файл", self.make_file)

        # Add currency
        self.add_currency.Text("Название", pady=1, col=1)
        self.add_currency.Entry(self.sn_textvar_ih, validatecommand=self.validate_text, pady=1,
                          col=1, widgetkwargs={"width": 30})
        self.add_currency.Text("Номер(DEC)", pady=1, col=2)
        self.add_currency.Entry(self.sn_textvar_ih, validatecommand=self.validate_text, pady=1,
                          col=2, widgetkwargs={"width": 30})
        self.add_currency.AccentButton("Добавить", self.make_file, col=1)
        self.add_currency.Button("Удалить", self.make_file, col=2)



        j = 0
        h = 0
        for i in range(56):
            h += 1
            if i % 7 == 0:
                j += 1
                h = 0
            self.tab_1.Checkbutton("RUB", self.checkbox1, self.printcheckboxvars, (1,), col=h, row=j)
            print(f"{i}, {j}")

        self.run()

    def validate_text(self, text):
        if self == self:
            pass
        if 'q' not in text:
            return True
        print("The letter q is not allowed.")
        return False

    def printcheckboxvars(self, number):
        print("Checkbox number:", number, "was pressed")
        print("Checkboxes: ", self.checkbox1.get(), self.checkbox2.get())

    def make_file(self):
        pass



if __name__ == "__main__":
    App("park", "dark")
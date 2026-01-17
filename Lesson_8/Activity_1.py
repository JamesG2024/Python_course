import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

class DenominationCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Denomination Calculator")
        self.root.geometry("600x700")
        self.root.resizable(True, True)
        self.root.config(bg="#B3C9DF")

        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after_idle(self.root.attributes, '-topmost', False)
        


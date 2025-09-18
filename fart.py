import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('demo')
window.geometry('1280x720')

title_label = ttk.Label(master = window, text = "hello world")
window.mainloop()

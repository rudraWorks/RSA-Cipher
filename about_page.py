import tkinter as tk

def about_page(main_frame):
    about_frame = tk.Frame(main_frame)
    lb = tk.Label(about_frame, text='about', font=("bold", 30))
    lb.pack()
    about_frame.pack(pady=20)

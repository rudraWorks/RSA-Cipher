import tkinter as tk

def home_page(main_frame):
    frame = tk.Frame(main_frame)
    lb = tk.Label(frame, text='home', font=("bold", 30))
    lb.pack()
    frame.pack(pady=20)

    def show():
        tk.Label(frame, text="hi").pack()

    tk.Button(frame, text="click", command=show).pack()

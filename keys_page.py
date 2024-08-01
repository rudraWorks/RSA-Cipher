import tkinter as tk
from key_generation import create_key_generation_ui
from utils import check_keys

def keys_page(main_frame, indicate=None, home_indicate=None, home_page=None):
    def refresh_keys_page():
        delete_pages()
        keys_page(main_frame, indicate, home_indicate, home_page)

    def delete_pages():
        for widget in main_frame.winfo_children():
            widget.destroy()

    frame = tk.Frame(main_frame)
    lb = tk.Label(frame, text='Keys', font=("bold", 30))
    lb.pack()
    frame.pack(pady=20)

    status_label = tk.Label(frame, text='',font=("Bold",15))
    status_label.pack(pady=10)

    status,is_key_exist,p,q,e,phi,d,n = check_keys()

    status_label.config(text=status)

    if not is_key_exist:
        create_key_generation_ui(main_frame, refresh_keys_page)

    else:
        titleSize = 13

        tk.Label(main_frame,text="p",font=("Bold",titleSize)).pack()
        tk.Label(main_frame,text=str(p)).pack()

        tk.Canvas(main_frame, height=1, bg='black', width=480).pack()

        tk.Label(main_frame,text="q",font=("Bold",titleSize)).pack()
        tk.Label(main_frame,text=str(q)).pack()

        tk.Canvas(main_frame, height=1, bg='black', width=480).pack()

        tk.Label(main_frame,text="e",font=("Bold",titleSize)).pack()
        tk.Label(main_frame,text=str(e)).pack()

        tk.Canvas(main_frame, height=1, bg='black', width=480).pack()

        tk.Label(main_frame,text="phi",font=("Bold",titleSize)).pack()
        tk.Label(main_frame,text=str(phi),wraplength=480).pack()

        tk.Canvas(main_frame, height=1, bg='black', width=480).pack()

        tk.Label(main_frame,text="d",font=("Bold",titleSize)).pack()
        tk.Label(main_frame,text=str(d),wraplength=480).pack()

        tk.Canvas(main_frame, height=1, bg='black', width=480).pack()

        tk.Label(main_frame,text="n",font=("Bold",titleSize)).pack()
        tk.Label(main_frame,text=str(n),wraplength=480).pack()

        tk.Canvas(main_frame, height=1, bg='black', width=480).pack()
        tk.Label(main_frame,text="Private key: (d,n)\nPublic key: (e,n)",font=("Bold",10)).pack()

        frame = tk.Frame(main_frame)
        frame.pack(pady=10)

        def copy_public_key():
            frame.clipboard_clear()
            frame.clipboard_append(str(e)+"+"+str(n))

        def copy_private_key():
            frame.clipboard_clear()
            frame.clipboard_append(str(d)+"+"+str(n))
    
        tk.Button(frame, text="Copy public key",command=copy_public_key).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Copy private key",command=copy_private_key).grid(row=0, column=1, padx=5)

    if indicate and home_indicate and home_page:
        button = tk.Button(main_frame, text='Go to Home', command=lambda: indicate(home_indicate, home_page))
        button.pack(pady=10)

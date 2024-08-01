import tkinter as tk
from home_page import home_page
from about_page import about_page
from encrypt_page import encrypt_page
from decrypt_page import decrypt_page
from keys_page import keys_page

width = 800 
height = 600
option_width = 150

root = tk.Tk()
root.geometry(f'{width}x{height}')
root.title('RSA')

def hide_indicators():
    # home_indicate.config(bg='darkgray')
    # about_indicate.config(bg='darkgray')
    encrypt_indicate.config(bg='darkgray')
    decrypt_indicate.config(bg='darkgray')
    keys_indicate.config(bg='darkgray')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='gray')
    delete_pages()
    page(main_frame)

options_frame = tk.Frame(root, bg='darkgray')

# home_btn = tk.Button(options_frame, text='Home', font=('Bold', 15), fg="black", bd=0, command=lambda: indicate(home_indicate, home_page))
# home_indicate = tk.Label(options_frame, text='', bg='darkgray')

# about_btn = tk.Button(options_frame, text='About', font=('Bold', 15), fg="black", bd=0, command=lambda: indicate(about_indicate, about_page))
# about_indicate = tk.Label(options_frame, text='', bg='darkgray')

encrypt_btn = tk.Button(options_frame, text='Encrypt', font=('Bold', 15), fg="black", bd=0, command=lambda: indicate(encrypt_indicate, encrypt_page))
encrypt_indicate = tk.Label(options_frame, text='', bg='darkgray')

decrypt_btn = tk.Button(options_frame, text='Decrypt', font=('Bold', 15), fg="black", bd=0, command=lambda: indicate(decrypt_indicate, decrypt_page))
decrypt_indicate = tk.Label(options_frame, text='', bg='darkgray')

keys_btn = tk.Button(options_frame, text='Keys', font=('Bold', 15), fg="black", bd=0, command=lambda: indicate(keys_indicate, lambda frame: keys_page(frame)))
keys_indicate = tk.Label(options_frame, text='', bg='darkgray')

# Use grid to manage layout

# home_btn.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
# home_indicate.grid(row=0, column=1, sticky="ns", padx=(0, 10))

# about_btn.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
# about_indicate.grid(row=1, column=1, sticky="ns", padx=(0, 10))

encrypt_btn.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
encrypt_indicate.grid(row=2, column=1, sticky="ns", padx=(0, 10))

decrypt_btn.grid(row=3, column=0, sticky="ew", padx=10, pady=10)
decrypt_indicate.grid(row=3, column=1, sticky="ns", padx=(0, 10))

keys_btn.grid(row=4, column=0, sticky="ew", padx=10, pady=10)
keys_indicate.grid(row=4, column=1, sticky="ns", padx=(0, 10))

options_frame.pack(side=tk.LEFT, fill='y')
options_frame.pack_propagate(False)
options_frame.configure(width=option_width, height=height)

main_frame = tk.Frame(root)

main_frame.pack(side=tk.LEFT, fill='both', expand=True)
main_frame.pack_propagate(False)
main_frame.configure(height=height, width=width - option_width)

# Set the home page as the default page
indicate(encrypt_indicate, encrypt_page)

root.mainloop()

import tkinter as tk
from utils import append_zeroes_till_7_bits,group_by_seven,plain_text_to_cipher_text

def encrypt_page(main_frame):
    frame = tk.Frame(main_frame)
    lb = tk.Label(frame, text='Encrypt', font=("bold", 30))
    lb.pack()
    frame.pack(pady=20)

    tk.Label(frame,text="Enter plain text",font=("Arial",10)).pack(pady=5)
    text_box = tk.Text(frame, height=10)
    text_box.pack()

    tk.Label(frame,text="Enter public key",font=("Arial",10)).pack(pady=5)
    public_key = tk.Entry(frame,width=107)
    public_key.pack()

    cipher_text_box = tk.Text(frame,state=tk.DISABLED, height=5)
    
    cipher_label = tk.Label(frame,text="Cipher text",font=("Arial",10))
    error_label = tk.Label(frame,text='')
    error_label.pack()


    def copy_to_clipboard():
        frame.clipboard_clear()
        frame.clipboard_append(cipher_text_box.get("1.0",tk.END).rstrip())

    copy_btn = tk.Button(frame,text="Copy cipher text",command=copy_to_clipboard)

    def start_encrypt():

        public_key_list = public_key.get().split('+')

        if(len(public_key_list)!=2):
            error_label.config(text='Invalid public key!')
            return 
        
        error_label.config(text='')

        e,n = public_key_list 

        if not e.isdigit() or not n.isdigit():
            error_label.config(text='Invalid public key!')
            return 

        e = int(e)
        n = int(n)

        plain_text_value = text_box.get("1.0",tk.END).strip()
        monolith_string = ''
        for char in plain_text_value:
            s = str(bin(ord(char)))[2:]
            s = append_zeroes_till_7_bits(s)
            monolith_string+=s 
        groups = group_by_seven(monolith_string)

        cipher = ''

        for i in groups:
            cipher += str(plain_text_to_cipher_text(i,e,n))+"."

        cipher = cipher[0:-1]
        # print(cipher)

        cipher_label.pack(pady=5)
        cipher_text_box.pack()  
        cipher_text_box.config(state=tk.NORMAL) 
        cipher_text_box.delete("1.0", tk.END) 
        cipher_text_box.insert("1.0", cipher)  
        cipher_text_box.config(state=tk.DISABLED) 
        copy_btn.pack(padx=20, pady=10)



    tk.Button(frame, text="Encrypt text", command=start_encrypt).pack(padx=20,pady=10)


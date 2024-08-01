import tkinter as tk
from utils import append_zeroes_till_7_bits,group_by_seven,cipher_text_to_plain_text,get_seven_chars

def decrypt_page(main_frame):
    frame = tk.Frame(main_frame)
    lb = tk.Label(frame, text='Decrypt', font=("bold", 30))
    lb.pack()
    frame.pack(pady=20)

    tk.Label(frame,text="Enter cipher text",font=("Arial",10)).pack(pady=5)
    text_box = tk.Text(frame, height=10)
    text_box.pack()

    tk.Label(frame,text="Enter private key",font=("Arial",10)).pack(pady=5)
    private_key = tk.Entry(frame,width=107)
    private_key.pack()

    plain_text_box = tk.Text(frame,state=tk.DISABLED, height=5)
    
    plain_label = tk.Label(frame,text="Plain text",font=("Arial",10))
    error_label = tk.Label(frame,text='')
    error_label.pack()


    def copy_to_clipboard():
        frame.clipboard_clear()
        frame.clipboard_append(plain_text_box.get("1.0",tk.END).rstrip())

    copy_btn = tk.Button(frame,text="Copy plain text",command=copy_to_clipboard)

    def start_decrypt():

        private_key_list = private_key.get().rstrip().strip().split('+')

        if(len(private_key_list)!=2):
            error_label.config(text='Invalid private key!')
            return 
        
        error_label.config(text='')

        d,n = private_key_list 

        if not d.isdigit() or not n.isdigit():
            error_label.config(text='Invalid private key!')
            return 

        d = int(d)
        n = int(n)

        groups = text_box.get("1.0",tk.END).strip().split('.')
        

        # print(groups)

        for i in range(len(groups)):
            groups[i] = int(groups[i])

        # print(groups)

        plain = ''

        for C in groups:
            k = get_seven_chars(str(bin(cipher_text_to_plain_text(C,d,n)))[2:])
            plain += k
        #     print(k,plain)
        # print(len(plain))
        # tk.Label(frame,text=plain).pack()
        plain_label.pack(pady=5)
        plain_text_box.pack()  
        plain_text_box.config(state=tk.NORMAL) 
        plain_text_box.delete("1.0", tk.END) 
        plain_text_box.insert("1.0", plain)  
        plain_text_box.config(state=tk.DISABLED) 
        copy_btn.pack(padx=20, pady=10)



    tk.Button(frame, text="Decrypt text", command=start_decrypt).pack(padx=20,pady=10)


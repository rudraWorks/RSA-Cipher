import tkinter as tk
from tkinter import ttk
from sympy import nextprime
from random import randint
import os
from utils import gcd,extended_gcd

def create_key_generation_ui(main_frame, refresh_keys_page):
    canvas = tk.Canvas(main_frame, width=400, height=300, bg='white')
    canvas.pack(padx=20, pady=20)

    progress = ttk.Progressbar(main_frame, orient="horizontal", length=200, mode="determinate")
    progress.pack(pady=20)
    progress['value'] = 0

    progressValue = 0
    randomDigits = ""
    p = 0
    q = 0

    def show_coordinates(event):
        nonlocal progressValue
        nonlocal randomDigits
        nonlocal p
        nonlocal q
        if p and q:
            return
        if progressValue > 95:
            progress['value'] = 100

            print(len(randomDigits))
            
            while len(randomDigits) < 350:
                randomDigits += str(randint(0, 9))

            p_str = randomDigits[0:80]
            q_str = randomDigits[80:160]

            p_str = str(int(p_str))
            q_str = str(int(q_str))

            while(len(p_str)<80):
                p_str += str(randint(0, 9))
            while(len(q_str)<80):
                q_str += str(randint(0, 9))

            p = nextprime(int(p_str))
            q = nextprime(int(q_str))

            phi = (p-1)*(q-1)
            e = 3

            while gcd(e,phi) != 1:
                e = nextprime(e)

            key = str(p)+str(q)+str(e)

            with open('key.txt', 'w') as file:
                file.write(key)

            done_button = tk.Button(main_frame, text="Done", command=refresh_keys_page)
            done_button.pack(pady=10)
            return

        digit = ((event.x + event.y) % 10)
        progressValue = (progressValue + digit / 25) % 100
        randomDigits += str(digit)
        progress['value'] = progressValue

    canvas.bind('<Motion>', show_coordinates)

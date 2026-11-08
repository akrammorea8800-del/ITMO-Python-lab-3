import tkinter as tk
import random


def generate_key():
    key = []
    for i in range(3):
        block = []
        for j in range(3):
            block.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        for j in range(2):
            block.append(random.choice('0123456789'))
        random.shuffle(block)
        key.append(''.join(block))
    key_label.configure(text='-'.join(key))


window = tk.Tk()
window.title('Tetris Keygen')
window.geometry('576x360')
window.resizable(0, 0)

bg_img = tk.PhotoImage(file='tetris.png')
label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

title_label = tk.Label(window, text='TETRIS KEYGEN', font=('Verdana', 20), bg='#17243D', fg='white')
title_label.place(relx=0.5, rely=0.3, anchor='center')

key_label = tk.Label(window, text='XXXXX-XXXXX-XXXXX', font=('Consolas', 20), bg='white')
key_label.place(relx=0.5, rely=0.5, anchor='center')

btn = tk.Button(window, text='Generate', font=('Verdana', 14), command=generate_key)
btn.place(relx=0.5, rely=0.7, anchor='center')

window.mainloop()

# ==================================================
# File: Oppgave_3.py
# Author: Thomas Waaler
# Info: Making a Tkinter window with some widgets
# ==================================================
import tkinter as tk

window = tk.Tk()
window.title("GUI Elements")

lbl_1 = tk.Label(window, text="Label 1")
lbl_2 = tk.Label(window, text="Label 2", bg="red", fg="white")
lbl_3 = tk.Label(window, text="Label 3", bg="yellow", width=10, height=5)

btn_1 = tk.Button(window, text="Button!", width=7, height=2)
ent_1 = tk.Entry(window, width=15)
txt_1 = tk.Text(window)

lbl_1.pack()
lbl_2.pack()
lbl_3.pack()
btn_1.pack()
ent_1.pack()
txt_1.pack()

window.mainloop()
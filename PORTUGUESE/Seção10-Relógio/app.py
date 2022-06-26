from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Relógio")

def relogio():
  horario = strftime("%H:%M:%S")
  label.config(text=horario)
  label.after(1000, relogio)

label = Label(root, font=("Helvetica", 60), background="#7B68EE", foreground="#F0F8FF")
label.pack(anchor="center")

relogio()

mainloop()
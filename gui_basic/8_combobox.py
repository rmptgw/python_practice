from tkinter import ttk
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("TG GUI for python")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5,values=values)
combobox.pack()
combobox.set("카드 결제일")

readonly_combobox = ttk.Combobox(root, height=10,values=values, state="readonly")
readonly_combobox.current(0)
readonly_combobox.pack()

def btncmd(): # 선택된 값 표시
    print(combobox.get())
    print(readonly_combobox.get())
    

btn = Button(root, text='주문', command=btncmd)
btn.pack()

root.mainloop()
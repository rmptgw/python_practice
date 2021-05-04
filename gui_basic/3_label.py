from tkinter import *

root = Tk()

root.title("TG GUI for python")

label1 = Label(root, text="안녕하세요.")
label1.pack()

photo = PhotoImage( file = "gui_basic/tmp.enemy.png")
label2 = Label(root, image=photo)
label2.pack()

root.mainloop()
from tkinter import *

root = Tk()

root.title("TG GUI for python")
root.geometry("640x480")

chk_var = IntVar() # chk_var에 int형으로 값을 저장한다.
chk = Checkbutton(root, text='오늘 하루 보지 않기', variable=chk_var)
chk.select() # 자동 선택
chk.pack()

chk_var2 = IntVar()
chk2 = Checkbutton(root, text='일주일동안 보지 않기', variable=chk_var2)
chk2.select() # 자동 선택
chk2.pack()

def btncmd():
    # chk.deselect() # 선택 해제

    print(chk_var.get()) # 0 : 체크 해제, 1 : 체크
    print(chk_var2.get()) # 0 : 체크 해제, 1 : 체크

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()
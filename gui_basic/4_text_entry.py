from tkinter import *

root = Tk()

root.title("TG GUI for python")
root.geometry("640x480")


# 여러 줄을 받음
txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, '글자를 입력하세요')

# Entry = 한줄만 받음
e = Entry(root, width=30)
e.pack()
e.insert(END, '한 줄만 입력해요.')

def btncmd():
    print(txt.get("1.0", END)) # 1: 첫번째 라인, 0: 0번째 column 위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0,END)

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()
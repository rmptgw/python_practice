import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("TG GUI for python")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar.start(5) # 10ms 마다 움직임
# progressbar.pack()

# progressbar2 = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar2.start(10) # 10ms 마다 움직임
# progressbar2.pack()

p_var2 = DoubleVar()
progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar3.pack()


def btncmd(): # 선택된 값 표시
    # progressbar.stop() # 작동중지
    # progressbar2.stop() # 작동중지
    pass
def btncmd2(): # 선택된 값 표시
    # progressbar.stop() # 작동중지
    # progressbar2.stop() # 작동중지
    for i in range(1,101):
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # progress bar의 값 설정
        progressbar3.update() # ui 업데이트
        print(p_var2.get())

btn = Button(root, text='시작', command=btncmd2)
btn.pack()

root.mainloop()
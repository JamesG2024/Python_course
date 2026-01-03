
from tkinter import *
root = Tk()
root.geometry("400x300")
root.title('main')
def topwin():
    top = Toplevel()
    top.geometry("300x200")
    top.title("toplevel")
    l2 = Label(top, text = "This is toplevel window")
    l2.pack()
    top.mainloop()
l = Label(root, text= "This is root window")
btn = Button(root, text="Click here to open anpther window", command = topwin)
l.pack()
btn.pack()
root.mainloop()
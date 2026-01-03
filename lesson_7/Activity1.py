
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("image")
root.geometry("800x700")
upload = Image.open("img.png")
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, height=700, width=800)
label.place(x=50, y=0)
label2 = Label(root, text="This is howyou add image in Tkiner window")
label2.place(x=40, y=360)
root.mainloop()
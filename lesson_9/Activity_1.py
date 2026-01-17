from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# ---------------- MAIN WINDOW ----------------
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

# Image
upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

img_label = Label(root, image=image, bg='light blue')
img_label.image = image
img_label.place(x=180, y=20)

# Welcome text
label1 = Label(
    root,
    text="Hey User! Welcome to Denomination Counter Application.",
    bg='light blue',
    font=("Arial", 12)
)
label1.place(relx=0.5, y=340, anchor=CENTER)

# ---------------- TOP WINDOW FUNCTION ----------------
def topwin():
    top = Toplevel(root)
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")

    # Labels and Entry
    label = Label(top, text="Enter total amount", bg='light grey')
    label.place(x=230, y=50)

    entry = Entry(top)
    entry.place(x=200, y=80)

    btn = Button(
        top,
        text='Calculate',
        bg='brown',
        fg='white'
    )
    btn.place(x=240, y=120)

    lbl = Label(
        top,
        text="Here are number of notes for each denomination",
        bg='light grey'
    )
    lbl.place(x=140, y=170)

    # Denomination labels
    l1 = Label(top, text="2000", bg='light grey')
    l1.place(x=180, y=200)

    l2 = Label(top, text="500", bg='light grey')
    l2.place(x=180, y=230)

    l3 = Label(top, text="100", bg='light grey')
    l3.place(x=180, y=260)

    # Output entries
    t1 = Entry(top)
    t1.place(x=270, y=200)

    t2 = Entry(top)
    t2.place(x=270, y=230)

    t3 = Entry(top)
    t3.place(x=270, y=260)

    # Calculator logic
    def calculator():
        try:
            amount = int(entry.get())

            note2000 = amount // 2000
            amount %= 2000

            note500 = amount // 500
            amount %= 500

            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, note2000)
            t2.insert(END, note500)
            t3.insert(END, note100)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn.config(command=calculator)

# Button to open top window
open_btn = Button(
    root,
    text="Open Denomination Calculator",
    command=topwin,
    bg='brown',
    fg='white'
)
open_btn.place(relx=0.5, y=370, anchor=CENTER)

# ---------------- RUN APP ----------------
root.mainloop()

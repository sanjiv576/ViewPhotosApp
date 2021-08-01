from tkinter import *
root = Tk()
img = Image("photo", file="viewMe.icns")
# root.iconphoto(True, img) # you may also want to try this.
root.tk.call('wm','iconphoto', root._w, img)
img1 = PhotoImage(file="facebook.png")
img2 = PhotoImage(file="macOS.png")
img3 = PhotoImage(file="linkedin.png")
img4 = PhotoImage(file="twitter.png")
lst = [img1, img2, img3, img4]
rev = lst[::-1]
count = 1
reverse_count = 0
display = 0
Label(root, image=img1).grid(row=0, column=5)
def next():
    global count
    count += 1  #  2, 3, 4
    if count == len(lst):  # count = 5 True
        Button(root, text=">>>", state=DISABLED, command=next).grid(row=1, column=8)
        count = 0
    global display
    display = lst[count]
    Label(root, image=display).grid(row=0, column=5)


def previous():
    global reverse_count
    reverse_count += 1
    display = rev[reverse_count]
    Label(root, image=display).grid(row=0, column=5)



Button(root, text=">>>", command=next).grid(row=1, column=8)
Button(root, text="<<<", command=previous).grid(row=1, column=0)
Button(root, text="Exit", command=root.quit).grid(row=1, column=5)
Button(root, text=str(display) + " of " + str(len(lst))).grid(row=2, column=8)
root.mainloop()
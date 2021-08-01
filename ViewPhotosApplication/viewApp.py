"""This module is a basic application to display photos."""
from tkinter import *
viewer = Tk()
viewer.title("View Photos Application")
viewer.iconbitmap("iconView.ico")


img1 = PhotoImage(file="twitter.png")
img2 = PhotoImage(file="facebook.png")
img3 = PhotoImage(file="google.png")
img4 = PhotoImage(file="linkedin.png")
img5 = PhotoImage(file="macOS.png")
img6 = PhotoImage(file="whatsApp.png")
img7 = PhotoImage(file="windows.png")

Label(viewer, image=img1).grid(row=0, column=5)
all_images = [img1, img2, img3, img4, img5, img6, img7]
reverse_images = all_images[::-1]
counter = 1
display_pic = 0
reverse_count = len(all_images)


def next_image():
    global counter
    counter += 1  # 2, 3, 4, 5, 6, 7, 8
    global display_pic
    display_pic = all_images[counter-1]  # 1, 2, 3, 4, 5, 6, 7
    if counter <= len(all_images)+1:
        Label(viewer, text=str(counter) + " of " + str(len(all_images)), bd=3, relief=SUNKEN).grid(row=2, column=8)
        Label(viewer, image=display_pic).grid(row=0, column=5)
    if counter >= len(all_images):
        Button(viewer, text=">>>", font=("Courier", 15), state=DISABLED, command=next_image).grid(row=1, column=8)
    if counter > 1:
        Button(viewer, text="<<<", font=("Courier", 15), command=previous_image).grid(row=1, column=0)


def previous_image():
    global counter
    counter -= 1  # 8, 7, 6, 5, 4, 2, 1
    global display_pic
    display_pic = all_images[counter-1]  # 7, 6, 5, 4, 3, 2, 1
    if counter <= len(all_images)+1:
        Label(viewer, text=str(counter) + " of " + str(len(all_images)), bd=3, relief=SUNKEN).grid(row=2, column=8)
        Label(viewer, image=display_pic).grid(row=0, column=5)
    if counter < len(all_images):
        Button(viewer, text=">>>", font=("Courier", 15), command=next_image).grid(row=1, column=8)
    if counter <= 1:
        Button(viewer, text="<<<", font=("Courier", 15), state=DISABLED, command=previous_image).grid(row=1, column=0)


# Buttons defined

Button(viewer, text=">>>", font=("Courier", 15), command=next_image).grid(row=1, column=8)
Button(viewer, text="<<<", font=("Courier", 15), command=previous_image).grid(row=1, column=0)
Button(viewer, text="Exit", font=("Courier", 13), padx=15, pady=9, command=viewer.quit).grid(row=1, column=5)
Label(viewer, text="1 of " + str(len(all_images)), bd=3, relief=SUNKEN).grid(row=2, column=8)

viewer.mainloop()
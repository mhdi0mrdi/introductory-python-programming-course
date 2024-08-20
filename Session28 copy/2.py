from tkinter import *

form = Tk()

form.title("TODO editing form")
form.geometry("900x700")

form_image = PhotoImage(file=r"images/edit.png")
form.iconphoto(False, form_image)


sidebar = Frame(master=form, bg="#040536", width=200)
sidebar.pack(side=LEFT, fill=Y)
sidebar.propagate(False)

body = Frame(master=form, bg="white")
body.pack(fill=BOTH, expand=True)
body.propagate(False)

statusbar = Frame(
    master=body,
    bg="#eeeeee",
    height=23,
    highlightbackground="#00bcc9"
)

add_icon = PhotoImage(file=r"images/add.png")
Button(
    master=sidebar,
    text="  Edit",
    bg="#1a1b43",
    fg="white",
    activebackground="#17225c",
    activeforeground="white",
    pady=32,
    font=("tahoma", 11, "bold"),
    image=add_icon,
    compound=LEFT,
).pack(side=TOP, fill=X, padx=30, pady=(25, 0))

exit_icon = PhotoImage(file=r"images/exit.png")
Button(
    master=sidebar,
    text="  Exit",
    bg="#1a1b43",
    fg="white",
    activebackground="#17225c",
    activeforeground="white",
    pady=32,
    font=("tahoma", 11, "bold"),
    image=exit_icon,
    compound=LEFT,
).pack(side=TOP, fill=X, padx=30, pady=(25, 0))


form.mainloop()

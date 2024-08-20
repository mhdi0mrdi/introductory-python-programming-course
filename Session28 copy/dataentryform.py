from tkinter import BOTH, BOTTOM, Label, Tk, PhotoImage, LEFT, Y, X, Frame, Button, TOP


form = Tk()

# region config form
form.title("TODO Dataentry form")
form.geometry("850x520")
# form.resizable(width=False, height=False)


form_icon = PhotoImage(file=r"images/add.png")
form.iconphoto(False, form_icon)
# endregion

# region frame

sidebar = Frame(master=form, bg="#040536", width=200)
sidebar.pack(side=LEFT, fill=Y)
sidebar.propagate(False)

body = Frame(master=form, bg="white")
body.pack(fill=BOTH, expand=True)
body.propagate(False)

statusbar = Frame(
    master=body,
    bg="#eeeeee",
    height=20,
    highlightbackground="gray",
    highlightthickness=1
)
statusbar.pack(side=BOTTOM, fill=X)
statusbar.propagate(False)


title_frame = Frame(
    master=body,
    bg="red",
    height=45,
    highlightbackground="gray",
    highlightthickness=1
)
title_frame.pack(side=TOP, fill=X, padx=20, pady=20)
title_frame.propagate(False)

time_frame = Frame(
    master=body,
    bg="blue",
    height=45,
    highlightbackground="black",
    highlightthickness=1

)
time_frame.pack(side=TOP, fill=X, padx=20, pady=(0, 20))
time_frame.propagate(False)

status_frame = Frame(
    master=body,
    bg="green",
    height=45,
    highlightbackground="black",
    highlightthickness=1

)
status_frame.propagate(False)
status_frame.pack(side=TOP, fill=X, padx=20, pady=(0, 20))

description_frame = Frame(
    master=body,
    bg="green",
    height=45,
    highlightbackground="black",
    highlightthickness=1

)
description_frame.pack(fill=BOTH, expand=True, padx=20, pady=(0, 20))
description_frame.propagate(False)

# endregion

# region copyright
Label(
    master=statusbar,
    text="2024© Copyright",
    bg="#eeeeee",
    font=("tahoma", 7, "italic")
).pack(side=LEFT, padx=(10, 0))
# endregion

# region menu
add_icon = PhotoImage(file=r"images/add.png")
Button(
    master=sidebar,
    text="  Add",
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
    text=" Exit",
    bg="#1a1b43",
    fg="white",
    activebackground="#17225c",
    activeforeground="white",
    pady=32,
    font=("tahoma", 11, "bold"),
    image=exit_icon,
    compound=LEFT,
).pack(side=BOTTOM, fill=X, padx=30, pady=(25, 25))

# endregion


form.mainloop()

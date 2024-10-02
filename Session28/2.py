from tkinter import *
from tkinter.ttk import Treeview , Scrollbar

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

grid_scrollbar = Scrollbar(master=body, orient=VERTICAL)
grid_scrollbar.pack(side=RIGHT, fill=Y)


edit_grid = Treeview(
    master=body,
    columns=("name", "family", "phone", "status", "type"),
    show="headings",
    selectmode="extended",
    yscrollcommand=grid_scrollbar.set
)

edit_grid.heading(column="name", text="Name", anchor=CENTER)
edit_grid.heading(column="family", text="Family", anchor=CENTER)
edit_grid.heading(column="phone", text="Phone", anchor=CENTER)
edit_grid.heading(column="status", text="Status", anchor=CENTER)
edit_grid.heading(column="type", text="Type", anchor=CENTER)

edit_grid.column(column="name", anchor=CENTER,width=1)
edit_grid.column(column="family", anchor=CENTER,width=1)
edit_grid.column(column="phone", anchor=CENTER,width=1)
edit_grid.column(column="status", anchor=CENTER,width=1)
edit_grid.column(column="type",anchor=CENTER,width=1)

edit_grid.pack(fill=BOTH, expand=True)
grid_scrollbar["command"] = edit_grid.yview

menu_bar = Menu(master=form)

edit_menu = Menu(menu_bar,tearoff=0)
edit_menu.add_command(label="Add")
edit_menu.add_separator()
edit_menu.add_command(label="exit")

help_menu = Menu(menu_bar,tearoff=0)
help_menu.add_command(label="Help")

menu_bar.add_cascade(label="Edit managment",menu=edit_menu)
menu_bar.add_cascade(label="Help",menu=help_menu)

form.config(menu=menu_bar)

form.mainloop()

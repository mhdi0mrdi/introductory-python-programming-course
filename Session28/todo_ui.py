from tkinter import Menu, BOTH, BOTTOM, CENTER, RIGHT, W, Label, Tk, PhotoImage, LEFT, Y, X, Frame, Button, TOP, Toplevel
from tkinter.ttk import Treeview, Scrollbar


def main_form():

    def add_btn_onclick():
        form.withdraw()
        dataentry_form()
        form.deiconify()

    form = Tk()

    # region config form

    form_width = 850
    form_height = 520
    pad_x = (form.winfo_screenwidth()//2) - (form_width//2)
    pad_y = (form.winfo_screenheight()//2) - (form_height//2)

    form.title("TODO management system")
    form.geometry(f"{form_width}x{form_height}+{pad_x}+{pad_y}")
    # form.resizable(width=False, height=False)

    form_icon = PhotoImage(file=r"images/add.png")
    form.iconphoto(False, form_icon)

    form.configure(bg="white")
    # endregion

    # region frame

    sidebar = Frame(master=form, bg="#040536", width=200)
    sidebar.pack(side=LEFT, fill=Y)
    sidebar.propagate(False)

    body = Frame(master=form, bg="white")
    body.pack(fill=BOTH, expand=True, padx=25, pady=25)
    body.propagate(False)

    statusbar = Frame(
        master=form,
        bg="#eeeeee",
        height=20,
        highlightbackground="gray",
        highlightthickness=1
    )
    statusbar.pack(side=BOTTOM, fill=X)
    statusbar.propagate(False)

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
        font=("tahoma", 11, "bold"),
        image=add_icon,
        compound=LEFT,
        command=add_btn_onclick
    ).pack(side=TOP, fill=BOTH, expand=True, padx=30, pady=(25, 0))

    edit_icon = PhotoImage(file=r"images/edit.png")
    Button(
        master=sidebar,
        text="  Edit",
        bg="#1a1b43",
        fg="white",
        activebackground="#17225c",
        activeforeground="white",
        font=("tahoma", 11, "bold"),
        image=edit_icon,
        compound=LEFT,
    ).pack(side=TOP, fill=BOTH, expand=True, padx=30, pady=(25, 0))

    remove_icon = PhotoImage(file=r"images/remove.png")
    Button(
        master=sidebar,
        text=" Remove",
        bg="#1a1b43",
        fg="white",
        activebackground="#17225c",
        activeforeground="white",
        font=("tahoma", 11, "bold"),
        image=remove_icon,
        compound=LEFT,
    ).pack(side=TOP, fill=BOTH, expand=True, padx=30, pady=(25, 0))

    exit_icon = PhotoImage(file=r"images/exit.png")
    Button(
        master=sidebar,
        text=" Exit",
        bg="#1a1b43",
        fg="white",
        activebackground="#17225c",
        activeforeground="white",
        font=("tahoma", 11, "bold"),
        image=exit_icon,
        compound=LEFT,
    ).pack(side=TOP, fill=BOTH, expand=True, padx=30, pady=(25, 25))

    # endregion

    # region grid

    grid_scrollbar = Scrollbar(master=body, orient="vertical")
    grid_scrollbar.pack(side=RIGHT, fill=Y)

    todo_grid = Treeview(
        master=body,
        columns=("code", "title", "time", "status"),
        show="headings",
        selectmode="extended",
        yscrollcommand=grid_scrollbar.set
    )

    todo_grid.heading(column="code", text="ID", anchor=CENTER)
    todo_grid.heading(column="title", text="TODO title", anchor=CENTER)
    todo_grid.heading(column="time", text="TODO time", anchor=CENTER)
    todo_grid.heading(column="status", text="Status", anchor=CENTER)

    todo_grid.column(column="code", anchor=CENTER, width=1)
    todo_grid.column(column="title", anchor=CENTER, width=1)
    todo_grid.column(column="time", anchor=CENTER, width=1)
    todo_grid.column(column="status", anchor=CENTER, width=1)

    todo_grid.pack(fill=BOTH, expand=True)

    grid_scrollbar["command"] = todo_grid.yview

    # endregion

    for i in range(1, 100):
        todo_grid.insert("", "end", values=(
            f"{i}", f"title{i}", f"202{i}", "active"))

    # region menu

    menubar = Menu(master=form)

    todo_menu = Menu(menubar, tearoff=0)
    todo_menu.add_command(label="Add")
    todo_menu.add_separator()
    todo_menu.add_command(label="Exit")

    help_menu = Menu(menubar, tearoff=0)
    help_menu.add_command(label="Help")

    menubar.add_cascade(label="Todo manegment", menu=todo_menu)
    menubar.add_cascade(label="Help", menu=help_menu)

    form.config(menu=menubar)

    # endregion

    form.mainloop()


def dataentry_form():

    def back_btn_onclick():
        form.quit()
        form.destroy()

    form = Toplevel()

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
        text=" Back",
        bg="#1a1b43",
        fg="white",
        activebackground="#17225c",
        activeforeground="white",
        pady=32,
        font=("tahoma", 11, "bold"),
        image=exit_icon,
        compound=LEFT,
        command=back_btn_onclick
    ).pack(side=BOTTOM, fill=X, padx=30, pady=(25, 25))

    # endregion

    form.mainloop()


main_form()

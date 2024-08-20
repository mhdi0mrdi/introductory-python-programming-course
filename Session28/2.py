from tkinter import *

form = Tk()

form.title("TODO editing form")
form.geometry("900x700")

form_image = PhotoImage(file=r"images/edit.png")
form.iconphoto(False, form_icon)


sidebar = Frame(master=form, bg="#040536" , width = 200)
sidebar.pack(site=LEFT , fill=Y)
sidebar.propagate(False)

body = Frame(master=form , bg="white")
body.pack(fill=BOTH, expand=True)
body.propagate(False)

statusbar = Frame(
    master=body,
    bg="eeeeee",
    height=23,
    highlightbackground="000bcc9"




)







form.mainloop()
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Wierd")
root.geometry("1600x1600")

elements = ["Label", "Button", "Dropdown"]
DropDown = ttk.Combobox(root, state="readonly", values=elements)
DropDown.pack()


class CreateElements:
    def __init__(self):
        print("Everything is not working")

    def createLabel(self):
        label = Label(root, text="This Is A Label")
        label.pack()

    def createButton(self):
        btn = Button(root, text="Click Me")
        btn.pack()

    def createDropdown(self):
        elementss = [1, 2, 3]
        DropDown2 = ttk.Combobox(root, state="readonly", values=elementss)
        DropDown2.place()

    def choose(self):
        global DropDown
        TheSelected = DropDown.get()
        print(TheSelected)
        if TheSelected == "Label":
            self.createLabel()
        elif TheSelected == "Button":
            self.createButton()
        else:
            self.createDropdown()


obj1 = CreateElements()

thebtn = Button(root, text="Create Elements", command=obj1.choose)
thebtn.pack()

root.mainloop()

from tkinter import *
from tkinter import filedialog

root = Tk("Text editor")
text = Text(root)
text.grid()

def saveAs():
    global text

    t = text.get("1.0","end-1c")
    saveLocation = filedialog.asksaveasfilename()
    file1 = open(saveLocation,"w+")
    file1.write(t)
    file1.close()

button = Button(root,text="Save as",command=saveAs)
button.grid()

def fontHelvetica():
    global text
    text.config(font="Helvetica")

def fontCourier():
    global text
    text.config(font="Courier")


font = Menubutton(root,text="Font")
font.grid()
font.menu= Menu(font,tearoff=0)
font["menu"] = font.menu
helvetica = IntVar()
courier = IntVar()

font.menu.add_checkbutton(label="Courier",variable=courier,command=fontCourier)
font.menu.add_checkbutton(label="Helvetica",variable=helvetica,command=fontHelvetica)

root.mainloop()

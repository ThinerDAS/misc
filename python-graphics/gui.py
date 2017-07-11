#!/usr/bin/python -i

# Graphic programming snippet using python

# collected from Internet

from Tkinter import *
'''
class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
'''

import ttk
from PIL import *  #Image, ImageTk

root = Tk()

tree = ttk.Treeview(root)

tree["columns"] = ("one", "two")
tree.column("one", width=100)
tree.column("two", width=100)
tree.heading("one", text="coulmn A")
tree.heading("two", text="column B")

tree.insert("", 0, text="Line 1", values=("1A", "1b"))

id2 = tree.insert("", 1, "dir2", text="Dir 2")
tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A", "2B"))

##alternatively:
tree.insert("", 3, "dir3", text="Dir 3")
tree.insert("dir3", 3, text=" sub dir 3", values=("3A", " 3B"))

tree.pack()

#photo=PhotoImage(file="~/Pictures/s1.png")
arr = [(i % 253, (i * 17 + 15) % 241, ((i * 17) / 256) % 255)
       for i in range(65536)]

im = PhotoImage(width=256, height=256)

im.put(
    tuple([
        tuple(["#%02x%02x%02x" % arr[i * 256 + j] for i in range(256)])
        for j in range(256)
    ]))

label = Label(root, image=im)
label.image = im  # keep a reference!
label.pack(side=RIGHT)

from graphviz import Digraph
import dot2tex

f = Digraph('finite_state_machine', format='png')
f.attr(rankdir='UD', size='5,5')

f.attr('node', shape='doublecircle')
f.node('LR_0')
f.node('LR_3')
f.node('LR_4')
f.node('LR_8')

f.attr('node', shape='circle')
f.edge('LR_0', 'LR_2', label='SS(B)')
f.edge('LR_0', 'LR_1', label='SS(S)')
f.edge('LR_1', 'LR_3', label='S($end)')
f.edge('LR_2', 'LR_6', label='SS(b)')
f.edge('LR_2', 'LR_5', label='SS(a)')
f.edge('LR_2', 'LR_4', label='S(A)')
f.edge('LR_5', 'LR_7', label='S(b)')
f.edge('LR_5', 'LR_5', label='S(a)')
f.edge('LR_6', 'LR_6', label='S(b)')
f.edge('LR_6', 'LR_5', label='S(a)')
f.edge('LR_7', 'LR_8', label='S(b)')
f.edge('LR_7', 'LR_5', label='S(a)')
f.edge('LR_8', 'LR_6', label='S(b)')
f.edge('LR_8', 'LR_5', label='S(a)')

im2 = PhotoImage(data=f.pipe())

label2 = Label(root, image=im2)
label2.image = im  # keep a reference!
label2.pack(side=RIGHT)

root.mainloop()

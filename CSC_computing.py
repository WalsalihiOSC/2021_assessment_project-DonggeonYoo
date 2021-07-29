from tkinter import *
root = Tk()
root.title("CSC_Computing")
root.geometry("960x540")

lbl_1 = Label(root, text = "CSC Computing")
lbl_1.place(x = 360, y = 100)
lbl_1.config(font = ('현대하모니 L', 25, 'bold'))

lbl_2 = Label(root, text = "Write your information")
lbl_2.place(x = 370, y = 200)
lbl_2.config(font = ('현대하모니 L', 18))

lbl_3 = Label(root, text = "Student name : ")
lbl_3.place(x = 330, y = 267)
lbl_3.config(font = ('현대하모니 L', 15))

txt = Entry(root)
txt.place(x = 500, y = 270)

btn = Button(root, text = "Next", width = 12, height = 3, command = lambda: selecting_level_win(root))
btn.place(x = 720, y = 400)

class selecting_level_win:
    def __init__(self, root):
        self.lbl = Label(root, text = "Select your calculation level")
        self.lbl.grid(row = 1, column = 1)
        
        var = StringVar()
        btn_1 = Radiobutton(root, text = "Level 1 (easiest)", value = 1, variable = var)
        #btn_1.grid()
        btn_2 = Radiobutton(root, text = "Level 2 (normal)", value = 2, variable = var)
        btn_3 = Radiobutton(root, text = "Level 3 (hardest)", value = 3, variable = var)
        btn_1.pack()
        btn_2.pack()
        btn_3.pack()

        btn = Button(root, text = "Next")
        btn.grid(row = 1, column = 2)
        btn.pack()

"""
class 
"""

root.mainloop()
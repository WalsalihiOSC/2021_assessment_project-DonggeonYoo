from tkinter import *
import random

class Main_win:
        def __init__(self, winde):
                self.wind = winde
                self.not_valid = False
        
        def interface(self):
                self.inter_face = Frame(self.wind)
                self.inter_face .grid()

                Label(self.inter_face ,text="CSC computing", font=('현대하모니 L', 25, 'bold')).grid(row=0, column=2)

                Label(self.inter_face, text = "Write your information", font =('현대하모니 L', 18,'underline')).place(x=115, y =70)
                # Studen Name 
                Label(self.inter_face, font=('현대하모니', 15), text="Student Name : ").place(x=105,y=120)
                # Studen name 

                Label(self.inter_face, font=('현대하모니', 15), text="  Studen age: ").place(x=115,y=170)
                
                # Studen age
                self.Sa = Entry(self.inter_face)
                self.Sa.place(x=280,y=175)
                # Studen name 
                self.Sn = Entry(self.inter_face)
                self.Sn.place(x=280,y=125)

                next=Button(self.inter_face, text="  Next ", font=50,bg="green",fg="black", command = self.selecting_level_win)
                next.place(x=400, y=240)
        
                Label(self.inter_face,text=" **** ",font="Arial 50 bold",fg="gray95").grid(column=3,row=1)
                Label(self.inter_face,text=" **** ",font="Arial 50 bold",fg="gray95").grid(column=3,row=2)
                Label(self.inter_face,text=" *** ",font="Arial 50 bold",fg="gray95").grid(column=1,row=3)
                
        def selecting_level_win(self):
                self.Studen_name = self.Sn.get().capitalize()
                self.Studen_age = self.Sa.get()
                if len(self.Studen_name) == 0 or len(self.Studen_age) == 0:
                        self.notvalid = True
                elif self.Studen_age not in ["6","7","8","9","10","11","12"]:
                        self.notvalid = True
                else:
                        self.inter_face.grid_forget()
                        self.level_win = Frame(self.wind)
                        self.level_win.grid()

                        Label(self.level_win, text = "Select your level",font = ('현대하모니 L', 25, 'bold')).grid(row=0, column=2)
                
                        self.var = IntVar()
                        btn_1 = Radiobutton(self.level_win, text = "Level 1 [Easiest]", font=('현대하모니 L', 15), value = 1, variable = self.var)
                        btn_1.place(x = 160, y = 100)
                        btn_2 = Radiobutton(self.level_win, text = "Level 2 [Normal]", font=('현대하모니 L', 15), value = 2, variable = self.var)
                        btn_2.place(x = 160, y = 130)
                        btn_3 = Radiobutton(self.level_win, text = "Level 3 [Hardest]", font=('현대하모니 L', 15), value = 3, variable = self.var)
                        btn_3.place(x = 160, y = 160)

                        Label(self.level_win,text=" **** ",font="Arial 50 bold",fg="gray95").grid(column=3,row=1)
                        Label(self.level_win,text=" **** ",font="Arial 50 bold",fg="gray95").grid(column=3,row=2)
                        Label(self.level_win,text=" *** ",font="Arial 50 bold",fg="gray95").grid(column=1,row=3)

                        next=Button(self.level_win, text="  Next ", font=50,bg="green",fg="black", command = self.qustion_win)
                        next.place(x=400, y=240)

        def qustion_win(self):

                if (self.var.get() ==1):
                        self.x = ["1","2","3","4","5"]
                        self.y = ["6","7","8","9","10"]
                        self.lev = "Easiest"
                elif (self.var.get() ==2):
                        self.x =["6","7","5","4","3"]
                        self.y = ["8","9","10","11","12"]
                        self.lev = "Normal"

                elif (self.var.get() ==3):
                        self.x = ["1","2","3","4","5","6","7","8","9"]
                        self.y = ["13","14","15","16","10","11","12"]
                        self.lev = "Hardest"

                self.level_win.grid_forget()
                self.qustions = Frame(self.wind)
                self.qustions.grid()
                self.count = 1
                Label(self.qustions, text = f"Select the answer [{self.lev}]",font = ('현대하모니 L', 25, 'bold')).grid(row=0, column=2)

                self.random_qustion()

                next=Button(self.qustions, text=" Submit ", font=50,bg="green",fg="black", command = lambda: self.submet(self.n))
                next.place(x=400, y=240)

                Label(self.qustions,text=" **** ",font="Arial 100 bold",fg="gray95").grid(column=3,row=1)
                Label(self.qustions,text=" **** ",font="Arial 50 bold",fg="gray95").grid(column=3,row=2)
                Label(self.qustions,text=" - ",font="Arial 30 bold",fg="gray95").grid(column=1,row=3)

        def random_qustion(self):
                
                self.A = random.choice(self.y)
                self.B =  random.choice(self.x)

                self.noting = random.randrange(30,100)
                
                Q_s = ('+', '-', 'x')
                self.Q = random.choice(Q_s)
                
                if self.Q == '+':
                        self.solve = int(self.A) + int(self.B)
                        self.qustion()

                elif self.Q == '-':
                        self.solve = int(self.A) - int(self.B)
                        self.qustion()
                        
                elif self.Q == 'x':
                        self.solve = int(self.A) * int(self.B)
                        self.qustion()     
        
        def answer(self):
                return self.solve
        
        def qustion(self):
                op = [self.noting , self.solve]
                self.l = random.choice(op)
                self.i = random.choice(op)
                question = Label(self.qustions, text=f"Q{self.count}) {self.A} {self.Q} {self.B} = ?",font=('현대하모니 L', 20, 'bold'))
                question.place(x= 170 , y = 100)
                
                self.n = IntVar()
                btn_1 = Radiobutton(self.qustions, text = f"{self.l}", font=('현대하모니 L', 15), value = 1, variable = self.n)
                btn_1.place(x = 130, y = 170)
                btn_2 = Radiobutton(self.qustions, text =f"{self.i}", font=('현대하모니 L', 15), value = 2, variable = self.n)
                btn_2.place(x = 320, y = 170)
                
        
        
        def submet(self,prob):
                # input == answer
                if self.l == self.solve:
                        self.n = self.k
                if self.i == self.solve:
                        self.n = self.k

                if prob.get() == str(self.answer()):
                        Label(self.qustions, text="✔️", fg="green",font="Arial 20 bold").place(x=500, y=160)
              
                        self.scoer_count += 1 
                        self.count += 1
                        self.nex =Button(self.qustions ,text="Next",bg="green",fg="black" ,font="Arial 14 bold",width=9,height=2,command = self.next ).place(x=510, y=300)
                else:
                        wrong = Label(self.qustions, text="❌", fg="red")
                        wrong.place(x=500, y=160)
                        self.count += 1
                        self.nex =Button(self.qustions ,text="Next",bg="green",fg="black" ,font="Arial 14 bold",width=9,height=2,command = self.next ).place(x=510, y=300)
                        Label(self.qustions ,text=f"The Answer is {self.answer_1}",font="Arial 14 bold").place(x=310, y=220)

                # button == 10 times 
                if self.count == 11:
                        # next Frame button
                        Button(self.qustions ,text="Exit",bg="cornflower blue",fg="black" ,font="Arial 14 bold",width=9,height=2,command = self.End_wind ).place(x=510, y=300)

root = Tk()


root.title("OSC Course Selection")
root.geometry("500x300")

gui = Main_win(root)

gui.interface()
root.mainloop()
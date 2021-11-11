from tkinter import *
import random
from CSC_computing_2 import *


class Main_win:
        def __init__(self, winde):
                self.wind = winde
                self.not_valid = False
                self.score = 0
        
        def interface(self):
                self.inter_face = Frame(self.wind)
                self.inter_face .grid()

                Label(self.inter_face ,text="CSC computing", font=('Calibri', 30, 'bold')).grid(row=0, column=2)

                Label(self.inter_face, text = "Write your information", font =('Calibri', 18,'underline')).place(x=135, y =70)
                # Studen Name 
                Label(self.inter_face, font=('Arial', 15), text="Student Name : ").place(x=105,y=120)
                # Studen name 

                Label(self.inter_face, font=('Arial', 15), text="  Studen age: ").place(x=115,y=170)
                
                # Studen age
                self.Sa = Entry(self.inter_face)
                self.Sa.place(x=280,y=175)
                # Studen name 
                self.Sn = Entry(self.inter_face)
                self.Sn.place(x=280,y=125)

                next=Button(self.inter_face, text="Next", font=50,bg="green",fg="black",width=7,height=1, command = self.selecting_level_win)
                next.place(x=400, y=240)
        
                Label(self.inter_face,text=" **** ",font="Arial 50 bold",fg="gray95").grid(column=3,row=1)
                Label(self.inter_face,text=" **** ",font="Arial 50 bold",fg="gray95").grid(column=3,row=2)
                Label(self.inter_face,text=" *** ",font="Arial 50 bold",fg="gray95").grid(column=1,row=3)
                
        def selecting_level_win(self):
                self.Studen_name = self.Sn.get().capitalize()
                self.Studen_age = self.Sa.get()
                self.stud = Student(self.Studen_name, self.Studen_age)

                if len(self.Studen_name) == 0 or len(self.Studen_age) == 0:
                        self.notvalid = True
                elif self.Studen_age not in ["6","7","8","9","10","11","12"]:
                        self.notvalid = True
                else:
                        self.inter_face.grid_forget()
                        self.level_win = Frame(self.wind)
                        self.level_win.grid()

                        Label(self.level_win, text = "Select your level",font = ('Calibri', 25, 'bold')).grid(row=0, column=2)
                
                        self.var = IntVar()
                        btn_1 = Radiobutton(self.level_win, text = "Level 1 [Easiest]", font=('Calibri', 15), value = 1, variable = self.var)
                        btn_1.place(x = 160, y = 100)
                        btn_2 = Radiobutton(self.level_win, text = "Level 2 [Normal]", font=('Calibri', 15), value = 2, variable = self.var)
                        btn_2.place(x = 160, y = 130)
                        btn_3 = Radiobutton(self.level_win, text = "Level 3 [Hardest]", font=('Calibri', 15), value = 3, variable = self.var)
                        btn_3.place(x = 160, y = 160)

                        Label(self.level_win,text=" **** ",font="Arial 50 bold",fg="gray95").grid(column=3,row=1)
                        Label(self.level_win,text=" **** ",font="Arial 50 bold",fg="gray95").grid(column=3,row=2)
                        Label(self.level_win,text=" *** ",font="Arial 50 bold",fg="gray95").grid(column=1,row=3)

                        next=Button(self.level_win, text="Next", font=50,bg="green",fg="black",width=7,height=1, command = self.qustion_win)
                        next.place(x=400, y=240)

        def qustion_win(self):
                if (self.var.get() == 0):
                    self.notvalid = True

                elif (self.var.get() ==1):
                        num_1 , num_2 = self.stud.lev_1()
                        self.x = (num_2)
                        self.y = (num_1)
                        self.lev = "Easiest"
                elif (self.var.get() ==2):
                        num_1 , num_2 = self.stud.lev_2()
                        self.x = (num_2)
                        self.y = (num_1)
                        self.lev = "Normal"
        
                elif (self.var.get() ==3):
                        num_1 , num_2 = self.stud.lev_2()
                        self.x = (num_2)
                        self.y = (num_1)
                        self.lev = "Hardest"

                self.level_win.grid_forget()
                self.qustions = Frame(self.wind)
                self.qustions.grid()
                self.count = 1
                Label(self.qustions, text = f"Select the answer [{self.lev}]",font = ('Calibri', 25, 'bold')).grid(row=0, column=2)

                self.random_qustion()

                next=Button(self.qustions, text="Submit", font=50,bg="cornflower blue",fg="black",width=7,height=1, command = lambda: self.submit(self.pa))
                next.place(x=400, y=240)

                Label(self.qustions,text=" **** ",font="Arial 100 bold",fg="gray95").grid(column=3,row=1)
                Label(self.qustions,text=" **** ",font="Arial 50 bold",fg="gray95").grid(column=3,row=2)
                Label(self.qustions,text=" - ",font="Arial 30 bold",fg="gray95").grid(column=1,row=3)

        def random_qustion(self):
                
                self.A = random.choice(self.y)
                self.B =  random.choice(self.x)

                
                
                Q_s = ('+', '-', 'x')
                self.Q = random.choice(Q_s)
                self.noting = random.randrange(30,100) 

                if self.Q == '+':
                        self.solve = int(self.A) + int(self.B)
                        #Check if same
                        if self.noting == self.solve:
                                self.noting =- 5
                        self.Qustions()

                elif self.Q == '-':
                        self.solve = int(self.A) - int(self.B)
                        if self.noting == self.solve:
                                self.noting =- 5
                        self.Qustions()
                        
                elif self.Q == 'x':
                        self.solve = int(self.A) * int(self.B)
                        if self.noting == self.solve:
                                self.noting =- 5
                        self.Qustions()  

           
                
        
        def answer(self):
                return self.solve
        
        def Qustions(self):
                op = [self.noting , self.solve]
                self.l = random.choice(op)
                op.remove(self.l)
                self.r = op[0]
                question = Label(self.qustions, text=f"Q{self.count}) {self.A} {self.Q} {self.B} = ",font=('Calibri', 25, 'bold'))
                question.place(x= 100 , y = 120)
                 
                self.pa = Entry(self.qustions,font=('Calibri', 20))
                self.pa.place(x=320,y=130,width=100,height=25)
                
        
        
        def submit(self,answ):
                # input == answer
                # print(f'prob is: {prob}')
                # if self.l == self.solve:
                #         self.n = self.k
                # if self.r == self.solve:
                #         self.n = self.k
                
                # if prob.get() == str(self.answer()):
                Label(text = "n is: {self.n.get()}", font = ('Calibri', 10, 'bold')).grid
                print(f'answer is: {self.answer()}')
                

                if answ.get() == str(self.answer()):
                        print("Correct")
                        #TODO: Fix X Y coordinates
                        Label(self.qustions, text="✔️", fg="green").place(x=100, y=100)
              
                        self.score += 1 
                        self.count += 1
                        self.nextButton =Button(self.qustions ,text="Next", font=50,bg="green",fg="black" ,width=7,height=1,command = self.Next_button )
                        self.nextButton.place(x=400, y=240)
                else:
                        print("Wrong")
                        #TODO: Fix X Y coordinates
                        wrong = Label(self.qustions, text="❌", fg="red")
                        wrong.place(x=100, y=100)
                        self.count += 1
                        self.nextButton =Button(self.qustions ,text="Next", font=50,bg="green",fg="black" ,width=7,height=1,command = self.Next_button )
                        self.nextButton.place(x=400, y=240)

                # button == 10 times 
                if self.count == 11:
                        # next Frame button
                        Button(self.qustions ,text="Exit",bg="red",fg="black" ,font=50 ,width=7,height=1,command = self.Result_wind ).place(x=400, y=240)

        def Next_button (self):
            Label (self.qustions, text ="*****",fg="gray95").place(x=100, y=100)
            Label (self.qustions, text ="********************",font="Arial 20 bold",fg="gray95").place(x= 100 , y = 120)
            self.random_qustion()

            next=Button(self.qustions, text="Submit", font=50,bg="cornflower blue",fg="black",width=7,height=1 ,command = lambda: self.submit(self.pa))
            next.place(x=400, y=240)
    
        def Result_wind (self):
            self.qustions.grid_forget()
            self.stud.save(self.score)
            self.result = Frame(self.wind)
            self.result.grid()
            Label(self.result, text = f"Result",font = ('Calibri', 30, 'bold')).grid(row=0, column=2)
            Label(self.result, text = f" You got [{self.score}/10]",font = ('Calibri', 25, 'bold')).grid(row=1, column=2)

            Label(self.result,text=" ******** ",font="Arial 100 bold",fg="gray95").grid(column=3,row=5)
            Label(self.result,text=" ******** ",font="Arial 30 bold",fg="gray95").grid(column=1,row=3)
            Label(self.result,text=" ******** ",font="Arial 30 bold",fg="gray95").grid(column=1,row=4)


            New_player=Button(self.result, text="New_player", font=50,bg="green",fg="black",width=10,height=1 ,command =self.New_Player )
            New_player.place(x=205, y=150)

            New_game=Button(self.result, text="New_game", font=50,bg="green",fg="black",width=10,height=1 ,command = self.New_Game)
            New_game.place(x=205, y=200)
            
            Exit=Button(self.result, text="Exit", font=50,bg="green",fg="black",width=7,height=1 ,command = self.wind.destroy)
            Exit.place(x=225, y=250)
        
        def New_Player(self):
            self.result.destroy()
            self.level_win.grid() 
         
        def New_Game(self):
            self.result.destroy()
            self.interface()
            
root = Tk()


root.title("OSC Course Selection")
root.geometry("500x300")

gui = Main_win(root)

gui.interface()
root.mainloop()
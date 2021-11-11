
class Student:
    def __init__(self,sn,sa):
        self.Studen_name = sn
        self.Studen_age = sa

    def lev_1(self):
            num_1 = ["1","2","3","4","5"]
            num_2 = ["6","7","8","9","10"]
            return num_1 , num_2 ;

    def lev_2(self):
            num_1 = ["6","7","5","4","3"]
            num_2 = ["8","9","10","11","12"]
            return num_1 ,num_2 ;

    def lev_3(self):
            num_1 = ["1","2","3","4","5","6","7","8","9"]
            num_2 = ["13","14","15","16","10","11","12"]
            return num_1, num_2 ;
            
                
    def save(self,sc):
        player_file = open("Student_info_v1.text", "a")
        player_file.write("\Student Name: {} \Student age: {} \n" .format(self.Studen_name, self.Studen_age))
        player_file.write(f"You got [{sc}/10]\n")
        player_file.close()
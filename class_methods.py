# TYPES OF METHOD
 
class student():
    institution = "IIPS"
    def init(self,a,b):
        self.a = a
        self.b = b
       
    def show(self):
        print("--------------------------")
        print("Marks in python" , self.a)
        print("Marks in python Lab" , self.b)
        print("---------------------------")
# class method
    @classmethod    
    def info(self):
        print("class belongs to",self.institution)
       
    #static method
    @staticmethod
    def about():
        print("this class holds data of marks obtain by student in python")
       
       
       
       
s1 = student(12,10)
s2 = student(13,11)
s3 = student(14,9)

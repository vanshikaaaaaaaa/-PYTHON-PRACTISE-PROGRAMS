class test:
    def __init__(self,num1,num2):
      self.n1=num1
      self.n2=num2
    def show(self):
        print("--------")
        print(self.n1)
        print(self.n2)



    def __add__(self,other):
        x = self.n1 + other.n1
        y = self.n2 + other.n2
        z = test(x,y)
        return z
    
      
      

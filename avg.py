class student:
 
 def avg(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

 def avg(self,a=None,b=None,c=None):
        average=0
        if(a!=None and b!=None and c!=None):
            average=(a+b+c)/3
        elif(a!=None and b!=None and c==None):
            average=(a+b)/2
        elif(a!=None and b==None and c==None):
            average=a
        else:
          print("no values provided")
        return average
s1=student()
avg1=s1.avg()
avg2=s1.avg(4,5)
avg3=s1.avg(3,4,5)
avg4=s1.avg(3,4,5,6)

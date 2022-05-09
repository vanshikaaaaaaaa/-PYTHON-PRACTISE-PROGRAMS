class phonebook:
    def __init__(self,name,contact_no):
        self.name=name
        self.contact_no=contact_no
        

    def putdata(self):
        f=open("contact1.txt",'a')
        f.write("name")
        f.write("|")
        f.write(self.name)
        f.write("contact")
        f.write(self.contact_no)
        f.write("-----------------------------------")
        f.close()
        
    def getdata(self):
        
        f=open("contact1.txt",'r')
        x=f.read()
        print(x)
        f.close()
#n=int(input("enter no of times to take data"))
#for i in range(n):
c1=input("enter name")
c2=input("enter number")

c=phonebook(c1,c2)

c.putdata()
c.getdata()
    


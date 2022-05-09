'''a=1
b=2
c=3'''
user1=0 
user2=0
ch1=int(input("enter your choice: 1/2/3"))

ch2=int(input("enter second choice: 1/2/3"))
 
if(ch1==1 and ch2==2):
 print("user2 wins") 

elif(ch1==1 and ch2==3):
 print("user1 wins") 
 
elif(ch1==2 and ch2==1):
 print("user1 wins") 
 
elif(ch1==2 and ch2==3):
 print("user2 wins") 
 
elif(ch1==3 and ch2==1):
 print("user2 wins") 
 
elif(ch1==3 and ch2==2):
 print("user1 wins") 
else:
 print("draw") 

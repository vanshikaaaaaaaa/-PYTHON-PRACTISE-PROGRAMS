#print the divisors of a number
num=int(input("enter a number"))
for i in range(1,num):
    if num%i==0:
        print("divisor :",i)
else:
        print("divisor :",num)

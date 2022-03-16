def fibo(x):
 if x<=1:
     return 1
 else:
     return fibo(x-1) + fibo(x-2)
x=int(input("enter value"))
print("sequence is..")
for i in range(x):
    print(fibo(i)," ",end="")

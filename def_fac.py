def fact(x):
    y=1
    if x==1 or x==0:
        return y
    else:
        y=x*fact(x-1)
        return y
val=int(input("enter value"))
funct_val=fact(val)
print("factorial of {} is {}".format(val,funct_val))

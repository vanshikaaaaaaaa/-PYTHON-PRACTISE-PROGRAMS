a=int(input("enter 1st no."))
b=int(input("Emter 2nd no."))
c=int(input("Enter 3rd no."))
if a==b==c :
    print("all values are equal")
if a==b and c<b:
    print(a ,"and ", b ," are equal and ",c, "is less than" ,b)
elif b==c and a<b:
    print(b ,"and ", c ," are equal and ",a, "is less than" ,b)
elif a==c and b<a:
    print(a ,"and ", c ," are equal and ",b, "is less than" ,a)


if a==b and c>b:
    print(a ,"and ", b ," are equal and ",c, "is more than" ,b)
elif b==c and a>b:
    print(b ,"and ", c ," are equal and ",a, "is more than" ,b)
elif a==c and b>a:
    print(a ,"and ", c ," are equal and ",b, "is more than" ,a)

elif a>b and a>c:
    print(a ,"is greater than" ,b, "and", c)
elif b>a and b>c:
    print(b ," is greater than",a, "and",c)
else:
    print(c ,"is greater than",b, "and",a)

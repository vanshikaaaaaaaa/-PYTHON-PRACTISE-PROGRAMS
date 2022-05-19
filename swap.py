print("This script is intended to swap the values of two data variables using a third temporary variable")
a=(input("enter a string"))
b=(input("enter second string"))
print("without swapping",a,b)
'''
temp=a
a=b
b=temp
print("after swapping",a ,b)
print("values after swapping")

METHOD 2
a=a+b
b=a-b
a=a-b
'''

#METHOD 3
a,b=b,a
print("after swap=",a,b)

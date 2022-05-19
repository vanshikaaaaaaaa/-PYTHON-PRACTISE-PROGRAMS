from functools import reduce

# use filter function
# return "filter object"


list1 = [2,13,42,2,524,331,452,321,22]

list_even = list(filter(lambda x : x%2==0,list1))

list_odd = list(filter(lambda x : x%2==1,list1))

print(list_even)
print(list_odd)





# use map function

# multiple each element of a list





list_even12= [2, 42, 2, 524, 452, 22]

print("use reduce function")

sum = reduce(lambda x,y: x+y,list_even12)
print(sum)

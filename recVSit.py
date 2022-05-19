'''
write a python script to write the execution time for a variable in a file when
the variable is used to find factorial using iterative and recursion method
'''
import time
f=open("factorial.txt",'w')
current_time1=time.time()
#factorial by recursion
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
current_time2=time.time()
total_time=current_time2-current_time1
print("time is =",total_time)
#iteration
current_time3=time.time()
f=1
n=int(input("enter no"))
for i in range(1,n+1):
    f=f*i
print(f)
current_time4=time.time()
time=current_time4-current_time3
print("time=",time)
f.close()

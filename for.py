n=int(input("enter a nuber"))
m=n*10
count=1
for i in range(n,m+1,n):
     print("{} * {} = {}".format(n,count,i))
     count=count+1

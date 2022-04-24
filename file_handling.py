f=open("myfirstfile.txt",'w')
x='hiiiiiii'
y="hello bro\n"
f.write(y)
f.write('\n')
f.write(x)
f.close()
f=open("myfirstfile.txt",'r')
t=f.read()
print(t)

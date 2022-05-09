x="22+18/4-3"
exp=[]
y=list(x)
print("x=",y)
operand=""
for i in range(len(y)):
    if y[i]=="0" or y[i]=="1" or y[i]=="2" or y[i]=="3"  or y[i]=="4" or y[i]=="5" or y[i]=="6" or y[i]=="7" or y[i]=="8" or y[i]=="9":
      operand+=y[i] 
    elif y[i]=="+" or y[i]=="-" or y[i]=="/" or y[i]=="*":
      exp.append(operand)
      exp.append(y[i])
      operand = ""
    else:
        print("invalid")
exp.append(operand)
print("x=",exp)
        

w=int(input("enter weight"))
h=int(input("enter height"))
bmi=w/(h*h)
print(bmi)
if bmi<18.5:
      print("you are underweight")
elif bmi>=18.5 and bmi<25:
      print("you are normal")
elif bmi>=25 and bmi<30:
      print("you are overweight")
elif bmi>30:
      print("obesity")
else:
      print("")
   

print("this is a faulty calculator my bro")
a=float(input("give your no."))
b=float(input("your 2nd no."))
c=input("what you want? Press 1 for sum 2 for minus 3 for div and 4 for mul")
if a==45 and b==3 and c=="4":
    print(555)
elif a==56 and b==9 and c=="1":
    print(77)
elif c=="1":
    print(a+b)
elif c=="2":
    print(a-b)
elif c=="3":
    print(a/b)
elif c=="4":
    print(a*b)
else:
    print("Please input a correct number")
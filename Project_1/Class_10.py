a=0;b=0
choice=eval(input("Please Enter Youe choice:"))
# choice=int(choice)
if choice not in range(1,5):
    print("Invalid Choice")
if choice in range(1,5):
    a=eval(input("Please Enter 1st digit:"))
    b=eval(input("Please Enter 2st digit:"))
if choice==1:
    print("You choice is addition and the result is:{0}".format(a+b))
elif choice==2:
    if a>b:
        print("You choice is subtraction and the result is:"+str(a-b))
    else:
        print("You choice is subtraction and the result is:"+str(b-a))
elif choice==3:
    print("You choice is division and the result is:"+str(a/b))
elif choice==4:
    print("You choice is multiplication and the result is:"+str(a*b))
else:
    print("Try Again")

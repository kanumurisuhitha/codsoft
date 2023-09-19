while(True):
    n=int(input("Enter the number : "))
    m=int(input("Enter the number : "))
    s=input("Enter the character : ")
    if(s=='+'):
        print("Addition : ",m+n)
    elif(s=='-'):
        print("Subtraction : ",n-m)
    elif(s=='*'):
        print("Multiplication : ",m*n)
    elif(s=='/'):
        print("division : ",n/m)
    elif(s=='%'):
        print("remainder ",n%m)
    else:
        print("Invalid input")
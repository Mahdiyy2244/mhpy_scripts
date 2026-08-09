try:
    print("\t Welcome to my Caculator")
    print("-"*40)
    num1=float(input("\t Enter First Number : "))
    num2=float(input("\t Enter Secend Number : "))
    opr=input("Please Choise Your Operation Frop *,/,+,- : ")
    print("-"*40)
    if(opr=='*'):
        print("\t \t",num1*num2)
    elif(opr=='/'):
        if(num2>0):
            print("\t \t",num1/num2)
        else:
            print("\t A number cannot be divided by zero.".upper())
    if(opr=='+'):
        print("\t \t",num1+num2)
    elif(opr=='-'):
        print("\t \t",num1-num2)
except:
    print("The Entered Value Must be Numeric with Four basic Mathematical Mymbols.")    

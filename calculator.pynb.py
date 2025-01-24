def cal():

#Enter First Number
    a=int(input("Enter first Number"))

#Enter an Operator

    operator=(input("Enter Arthmetical Operator [+,-,*,/,%]\n"))
    if operator != "+" and operator !="-" and operator !="*" and operator !="/" and operator !="%":
     print("Arthmetical Operator Invalid")


#Enter Second Number

    b=int(input("Enter second Number"))

    if a==int and b==int :
      print(" ")
    else:
      print("Enter valid Number")

#Procedure of calculation

      if operator == "+" :
        res=a+b
        print("Addition : ",res)

      elif operator == "-" :
        res=a-b
        print("Subtraction : ",res)

      elif operator == "*" :
        res=a*b
        print("Multiplication : ",res)

      elif operator == "/" :
        res=a/b
        print("Division: ",res)

      elif operator == "%" :
       res=a%b
       print("Modulo : ",res)

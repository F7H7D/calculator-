j = 1



while j>0: 
    a = int(input("Enter first number : "))
    b = int(input("Enter first number : "))
    opar = input("Enter your oparetor(+,-,*,/) :")

    if opar == "+":
        print(f"The sum of 1st and 2nd num is : {a+b}")
    elif opar == "-":
        print(f"The sub of 1st and 2nd num is : {a-b}")
    elif opar == "*":
        print(f"The multiplication of 1st and 2nd is : {a*b}")
    elif opar == "/":
        print(f"The division of 1st and 2nd is : {a/b}")
    else:
        print("choose a oparetor")

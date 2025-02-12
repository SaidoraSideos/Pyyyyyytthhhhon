trigger = input("Do you want to perform a calculation?(Y)").upper().strip()
operator = "(?)"
while trigger == "Y" :
    try:
        Num1 = float(input("first number:"))
        print(f"{Num1} {operator}")
        Num2 = float(input("second number:"))
        print(f"{Num1} {operator} {Num2}")
        operator = input("Select (+, /, -, *)")

        if operator == "+":
          Result = Num1 + Num2
          print(Result)
        elif operator == "/":
          Result = Num1 / Num2
          print(Result)
        elif operator == "-":
          Result = Num1 - Num2
          print(Result)
        elif operator == "*":
          Result = Num1 * Num2
          print(Result)
        else:
          print("This is not an operator, dumbass")
          print(f"No calculation shall be carried out then")
        operator = "(?)"
        trigger == input("Do you wish to perform another calculation?(Y)")
    except ValueError:
       print ("I said enter numbers, Idiot.")
#ask for two numbers;
#    collect two numbers
#ask for an operator;
#    ask to use either div, multiply, sub, add
#do the calculation for the two numbers using the operator
#print the result

#number_one = int(input("Enter a number: "))
#number_two = int(input("Enter a number: "))


calculator_isRunning = True
while(calculator_isRunning):
    operator_choice = int(input("""

---------Choose an operator-----------
        1. to add
        2. to subtract
        3. to multiply
        4. to divide
        0. to exit calculator
    
        Choose an operator: """
        ))
    match(operator_choice):
        case 1:
            number_one = int(input("Enter a number: "))
            number_two = int(input("Enter a number: "))
            print(f"\n \tans= {number_one + number_two}")
        case 2:
            number_one = int(input("Enter a number: "))
            number_two = int(input("Enter a number: "))
            print(f"\n \tans= {number_one - number_two}")
        case 3:
            number_one = int(input("Enter a number: "))
            number_two = int(input("Enter a number: "))
            print(f"\n \tans= {number_one * number_two}")
        case 4:
            number_one = int(input("Enter a number: "))
            number_two = int(input("Enter a number: "))
            print(f"\n \tans= {number_one / number_two}")
        case 0:
            calculator_isRunning = False
            print("G O O D B Y E")
        case _:
            print("Invalid Operand")
          

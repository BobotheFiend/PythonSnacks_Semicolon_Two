#collect two inputs
#if the denominator is equals to zero no division happens
#else if the denominator is greater than 0 print result

numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter a denominator: "))

if denominator == 0:
    print("Cannot divide by zero")
else:
    division = numerator/denominator
    print(f"The division of {numerator}/{denominator} = {division}")

user_input = int(input("Enter a number: "))
counter = 0
print(f"The divisor(s) for {user_input} =",end=" ")
for count in range (1, user_input):
    counter+=1
    if user_input % counter == 0:
        print(f"{counter}",end=", ")
        

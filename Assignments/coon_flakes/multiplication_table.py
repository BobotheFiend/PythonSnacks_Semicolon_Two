#collect input, in this case 6
#multiply the input through the count from 1 = 10 displaying a result after each count
#print result

user_input = int(input("Enter a number: "))
multiply = 0
print(f"---------------------------------------------------------\n\tThe Multiplication Table for {user_input}\n---------------------------------------------------------")
for count in range(1,10+1):
    multiply = user_input * count
    print(f"{user_input} x {count} = {multiply}")


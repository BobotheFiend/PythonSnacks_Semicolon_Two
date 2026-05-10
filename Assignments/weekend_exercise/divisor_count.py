
user_input = int(input("Enter a number: "))
counter = 0
counting_divisor = 0
print(f"The divisor(s) count for {user_input} =",end=" ")
for count in range (1, user_input):
    counter+=1
    if user_input % counter == 0:
        counting_divisor+=1
        
print(f"{counting_divisor}",end=" ")

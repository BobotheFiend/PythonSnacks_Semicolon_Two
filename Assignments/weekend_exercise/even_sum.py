
number = int(input("Enter number: "))
total = 0
for count in range (2, number+1, 2):
    total+= count

print(f"The sum of the even numbers  = {total}")

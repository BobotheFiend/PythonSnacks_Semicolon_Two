#collect three inputs
#if the initial number is the largest
#compare it with the next number
#from that answer compare it with the next number
#then print the result

number_one = int(input("Enter a number: "))
number_two = int(input("Enter a number: "))
number_three = int(input("Enter a number: "))

largest = number_one
if number_two > number_one:
    largest = number_two
if number_three > largest:
    largest = number_three

print(f"The largest number = {largest}")

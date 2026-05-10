

user_input = input("Enter a number: ")

number_as_string = str(user_input)
reverse  = number_as_string[::-1]

if user_input == reverse:
    print(f"A palindrome!\n{user_input} ---> {reverse}")
else:
    print("Not a palindrome!")

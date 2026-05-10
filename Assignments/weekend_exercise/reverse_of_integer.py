#collect number
#convert it to string 
#use the string sclicing to start and stop from number and decrement
#print result

user_input = int(input("Enter a number: "))

number_as_string = str(user_input)
reverse  = int(number_as_string[::-1])

print(f"{user_input} reversed ---> {reverse}")

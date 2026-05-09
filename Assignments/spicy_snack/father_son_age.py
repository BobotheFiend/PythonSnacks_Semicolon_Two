#collect fathers age
#collect sons age
#from the fathers age calculate how old he will be twices as old as his son
#collect a new unknown variable and add it to both ages
#multiply the sons age by 2 and the variable
#collect like terms and find the unknown variable


father_age = int(input("WHat is the Fathers age?...  "))
son_age = int(input("What is the Son's age?...  "))


find_twice_the_age = 2 * son_age
the_future_age = father_age - find_twice_the_age
print(f" In {the_future_age} years \nThe father will be {father_age + the_future_age} years old \nThe son will be {son_age + the_future_age} years old \nWhich is twice as old as the son")



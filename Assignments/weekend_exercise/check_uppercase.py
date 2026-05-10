


user_input = input("Enter a word: ")

counter = 0
for count in user_input:
    if count in (["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]):
        counter+=1

print(f"{user_input} the amount of uppercase ---> {counter}")







user_input = input("Enter a word: ")

counter = 0
for count in user_input:
    if count in (["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]):

        counter+=1

print(f"{user_input} the amount of lowercase ---> {counter}")

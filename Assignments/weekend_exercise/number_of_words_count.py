

user_input = input("Enter a word: ")

counter = 0
for count in user_input:
    if count.lower() in (["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]):
        counter+=1        
print(f"The count of words in the sentence {user_input} = {counter}")

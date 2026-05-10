



user_input = input("Enter a word: ")
postion = 0
for count in user_input:
    postion+=1
    if count.lower() in (["a","e","i","o","u"]):
        print(f"the first vowel in {user_input} is {count} and the position is {postion}")
        break


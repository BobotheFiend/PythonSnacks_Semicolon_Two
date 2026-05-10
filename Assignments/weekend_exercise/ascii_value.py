user_input = input("Enter a word: ")

print(f"\tcharacter\t\tASCII VALUE\n----------------------------------------------")
for count in user_input:
    if count.lower() in (["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]):
        print(f"\t{count}\t\t\t{ord(count)}")

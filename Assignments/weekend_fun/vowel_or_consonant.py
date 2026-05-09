#collect a letter
#check to see if the letter collected matches the vowels
#if i does;
#    print vowel
#else if it doesnt
#    print consonant
#else
#    print invalid if not a letter

#import random
#
#letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#
#pick_at_random = random.choice(letters)
#
#if (pick_at_random.lower() in ["a","e","i","o","u"]):
#    print(f"{pick_at_random} is a Vowel!")
#elif (pick_at_random.lower() not in ["a","e","i","o","u"]):
#    print(f"{pick_at_random} is a Consonant!")
#else:
#    print(f"Invalid input")

letter = input("Enter a letter: ")

if (letter.lower() in ["a","e","i","o","u"]):
    print(f"{letter} is a Vowel!")
elif (letter.lower() not in ["a","e","i","o","u"]):        
    print(f"{letter} is a Consonant!")
else:
    print(f"Invalid Input!\n{letter} ")

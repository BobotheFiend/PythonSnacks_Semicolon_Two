#ticket pricing
#collect age
#use it to go through the list of requirments made for an age range
#if you are under 5....vfree entry
#if you are 5 - 12 ...12 dollar for entry
#if your are 13-64 ... entry fee 12 DOLLAR
#if your ARE 65+.... ENTRY FEE IS 8 DOLLAR


user_age = int(input("What is your age?.. "))

if user_age >= 0 and user_age < 5:
    print("Free Entry for you")
elif user_age >=5 and user_age <= 12:
    print("You're to pay $5")
elif user_age >= 13 and user_age <= 64:
    print("You're to pay $12")
elif user_age >=65 and user_age <= 150:
    print("You're to pay $8")
else:
    print("Not elligible")

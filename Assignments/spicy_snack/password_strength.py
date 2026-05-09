#password checker
#collect a value
#put it through a check list;
#    if the length is greater than 6 but less than 10... then its a medium psswd
#    if the length is less than 6... then it is a weak psswd
#    if the length is greater than 10 ... then it is a strong psswd
#    if the length is lesser than 1.. then it is an invalid psswd

def user_password(password):

    if len(password) > 6 and len(password) < 10:
        return "MEDIUM password!"
    elif len(password) >= 1 and len(password) <= 6:
        return "WEAK password!"
    elif len(password) >= 10 and len(password) <= 50:
        return "STRONG password!"
    else:
        return "Invalid password!"

user_choice = input("Enter a password: ")
password_strength = user_password(user_choice)
print(f"Your password strength is ---> {password_strength}")

#discount eligibility
#/collect total bill
#collect the evidence of membership
#apply discount if a member
#if the bill is above 1000 ... 10%off
#else if not a member... 5%off
#else no discount

total_bill = int(input("Enter bill total: "))

is_member = input("Is the person a member [Yes/No]?... ")

if (total_bill >= 1000 and is_member.lower() == "Yes".lower()):
    discount = total_bill - (total_bill * 0.10)
    print(f"Your new total bill to pay is {discount} \nThank you for being a Member")
elif (total_bill >= 1000 and is_member.lower() == "No".lower()):
    discount = total_bill - (total_bill *0.05)
    print(f"Your new total bill is {discount} \nWould you like to upgrade to Membership status?")
else:
    print(f"No discount! \nYour total bill to pay is {total_bill}")


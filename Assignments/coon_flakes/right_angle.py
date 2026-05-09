#collect input
#loop through until you meet the condition
#the first loop would serve as the counter
#the inner loop prints accordind to the counter numbers

number = int(input("Enter a number: "))

for count in range(1, number+1):
    for coloum in range(count, number+1):
        print("*",end="")

    print(" ")    

#collect input
#loop through until you meet the condition
#the first loop would serve as the counter
#the inner loop prints accordind to the counter numbers

number = int(input("Enter a number: "))

for count in range(number+1,0,-1):
    for coloumn in range(count):
        print(coloumn,end="")

    print(" ")    
